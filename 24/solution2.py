#!/usr/bin/env pypy3

from copy import deepcopy
import re
from functools import cache
from pprint import pprint
import sys
from z3 import *

rawwires,rawgates=open(sys.argv[1]).read().split('\n\n')

def color_decls(decl: str) -> str:
    if decl=='Xor':
        return f'\x1b\x5b31m{decl}\x1b\x5bm'
    elif decl=='Or':
        return f'\x1b\x5b32m{decl}\x1b\x5bm'
    elif decl=='And':
        return f'\x1b\x5b33m{decl}\x1b\x5bm'
    else:
        assert False

def highlight_decls(expr: str) -> str:
    return re.sub(r'\bAnd\b', color_decls('And'), re.sub(r'\bOr\b', color_decls('Or'), re.sub(r'\bXor\b', color_decls('Xor'), expr)))
def canon_str(expr, *, indent=' ', nl=True, d=0):
    children=expr.children()
    if not children:
        return f'{indent*d}{expr}' + ('\n' if nl else '')
    res=f'{indent*d}{expr.decl().__repr__()}(' + ('\n' if nl else '')
    s_children=[]
    for child in children:
        s_children.append(canon_str(child, indent=indent, nl=nl, d=d+1))
    s_children.sort(key=lambda x:(len(x),x))
    for i,s_child in enumerate(s_children):
        if i!=0:
            res+=','
        res+=s_child
    res+=f'{indent*d})' + ('\n' if nl else '')
    return res

gates={}
for l in rawwires.splitlines():
    w,v=l.split(': ')
    gates[w]=([int(v)], w)
    exec(f'{w} = Bool("{w}")')
op_lookup={'OR':'|', 'XOR':'^', 'AND':'&', }
for l in rawgates.splitlines():
    w12,w3=l.split(' -> ')
    w1,op,w2=w12.split()
    op=op_lookup[op]
    if w1 not in gates:
        gates[w1]=([-1], w1)
        exec(f'{w1} = Bool("{w1}")')
    if w2 not in gates:
        gates[w2]=([-1], w2)
        exec(f'{w2} = Bool("{w2}")')
    if w3 not in gates:
        gates[w3]=([-1], w3)
        exec(f'{w3} = Bool("{w3}")')
    gates[w3]=([w1, op, w2], f'{w1} {op} {w2}')
def evl(gate):
    assert gate in gates
    logic,_=gates[gate]
    if len(logic) == 1:
        if logic[0] in [0, 1]:
            return logic[0]
        assert False, f'indeterminate gate "{gate}": {logic[0]}'
    left,op,right=logic

    assert left in gates
    logic_left,_=gates[left]
    if len(logic_left) == 1 and logic_left[0] in [0, 1]:
        left_val=logic_left[0]
    else:
        left_val=evl(left)

    assert right in gates
    logic_right,_=gates[right]
    if len(logic_right) == 1 and logic_right[0] in [0, 1]:
        right_val=logic_right[0]
    else:
        right_val=evl(right)

    gates[gate] = ([eval(f'{left_val} {op} {right_val}')],
        re.sub(r'\((\w+)\)', r'\1', f'({gates[left][1]}) {op} ({gates[right][1]})'))
    return gates[gate][0][0]

for gate in gates:
    evl(gate)
for gate in deepcopy(gates):
    gates[gate]=(gates[gate][0], canon_str(eval(gates[gate][1]), indent='', nl=False))
def highest_gate(expr):
    max_var_idx=-1
    for boolvar in re.finditer(r'[xy]\d\d', expr):
        max_var_idx=max(int(boolvar[0][1:]), max_var_idx)
    return max_var_idx
#for gate in gates:
#    if gate[0] in 'z':
#        print(gate, highest_gate(gates[gate][1]))

#pprint(gates)
z_gates=[]
def update_z_gates():
    global z_gates
    z_gates=[]
    for gate in gates:
        if gate.startswith('z'):
            z_gates.append((gate,gates[gate][1]))
    z_gates.sort()
update_z_gates()
#print(json.dumps(z_gates, indent=4))

@cache
def gen_carry_z3(n):
    if n==0:
        return 'x00 & y00'
    return f'(x{n:02} & y{n:02}) | ((x{n:02} ^ y{n:02}) & ({gen_carry_z3(n-1)}))'

def gen_adder_z3(n):
    # n==0
    # x00 ^ y00
    # n==1
    # ((y00) & (x00)) ^ ((x01) ^ (y01))
    # n==2
    # ((y02) ^ (x02)) ^ (((x01) & (y01)) | (((x01) ^ (y01)) & ((y00) & (x00))))
    # n==3
    # (((((x01) & (y01)) | (((x01) ^ (y01)) & ((y00) & (x00)))) & ((y02) ^ (x02))) | ((x02) & (y02))) ^ ((y03) ^ (x03))
    if n==0:
        return 'x00 ^ y00'
    return f'(x{n:02} ^ y{n:02}) ^ ({gen_carry_z3(n-1)})'
def find_invalid_gate():
    for i,(gate,expr) in enumerate(z_gates):
        eq=eval(expr)
        s = Solver()
        if i<45:
            s.add(Not(eq == eval(gen_adder_z3(i))))
        else:
            s.add(Not(eq == eval(gen_carry_z3(i-1))))
        if s.check() == unsat:
            # print('correct', gate)
            pass
        else:
            # print('error', gate)
            return i
    return -1
def swap_outputs(i,j):
    z1=f'z{i:02}'
    z2=f'z{j:02}'
    gates[z1],gates[z2]=gates[z2],gates[z1]
    update_z_gates()
#swaps=[]
#err_z = find_invalid_gate()
#print('invalid gate', err_z)
#for i in range(err_z+1, 46):
#    swap_outputs(err_z, i)
#    new_err_z = find_invalid_gate()
#    if new_err_z == err_z:
#        swap_outputs(err_z, i)
#        continue
#    swaps.append((err_z,i))
#print(swaps)
def eq_same(a,b):
    s=Solver()
    s.add(Not(a==b))
    return s.check() == unsat

def find_invalid_gates():
    for i,(gate,expr) in enumerate(z_gates):
        eq=eval(expr)
        if i<45:
            eq2 = eval(gen_adder_z3(i))
        else:
            eq2 = eval(gen_carry_z3(i-1))
        if eq_same(eq, eq2):
            # print('correct', gate)
            pass
        else:
            print('error', gate)
            print('compared', eq)
            print('and', eq2)
#print(find_invalid_gate())
#a=eval(gates['z11'][1])
#b=eval(gen_adder_z3(11))
#print(highlight_decls(canon_str(a, indent='', nl=False)))
#print()
#print(highlight_decls(canon_str(b, indent='', nl=False)))
#print(eq_same(a, b))
#def print_gates(prefix):
#    z_gates=[]
#    for gate in gates:
#        if gate.startswith(prefix):
#            z_gates.append((gate,gates[gate][0][0]))
#    z_gates.sort(reverse=True)
#    print(bin(int(''.join(list(map(lambda tup:str(tup[1]), z_gates))), 2))[2:])

#print(end=' '); print_gates('x')
#print(end=' '); print_gates('y')
#print_gates('z')
#
#print()
#a=0b100000101010011010100101010101010010110100011
#b=0b100000101000101110010000000011011111011001101
#print(end=' '); print(bin(a)[2:])
#print(end=' '); print(bin(b)[2:])
#print(bin(a+b)[2:])

# z11

#raise SystemExit(0)
gates=dict(sorted(gates.items()))
for gate in gates:
    print(gate, highlight_decls(gates[gate][1]))
    if len(gate)==3 and gate.startswith('z'):
        num=int(gate[1:])
        print(gate, highlight_decls(canon_str(eval(gen_adder_z3(num) if num<45 else gen_carry_z3(num-1)), indent='', nl=False)))
    print()

# solved it by hand lol
