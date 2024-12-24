#!/usr/bin/env pypy3

rawwires,rawgates=open(0).read().split('\n\n')

gates={}
for l in rawwires.splitlines():
    w,v=l.split(': ')
    gates[w]=[int(v)]
op_lookup={'OR':'|', 'XOR':'^', 'AND':'&', }
for l in rawgates.splitlines():
    w12,w3=l.split(' -> ')
    w12=w12.replace(' OR ', ' OR  ')
    w1=w12[:3]
    op=w12[4:7]
    op=op.strip()
    op=op_lookup[op]
    w2=w12[8:]
    if w1 not in gates:
        gates[w1]=[-1]
    if w2 not in gates:
        gates[w2]=[-1]
    if w3 not in gates:
        gates[w3]=[-1]
    gates[w3]=[w1, op, w2]
def evl(gate):
    assert gate in gates
    logic=gates[gate]
    if len(logic) == 1:
        if logic[0] in [0, 1]:
            return logic[0]
        assert False, f'indeterminate gate "{gate}": {logic[0]}'
    left,op,right=logic

    assert left in gates
    logic_left=gates[left]
    if len(logic_left) == 1 and logic_left[0] in [0, 1]:
        left_val=logic_left[0]
    else:
        left_val=evl(left)

    assert right in gates
    logic_right=gates[right]
    if len(logic_right) == 1 and logic_right[0] in [0, 1]:
        right_val=logic_right[0]
    else:
        right_val=evl(right)

    gates[gate] = [eval(f'{left_val} {op} {right_val}')]
    return gates[gate][0]

for gate in gates:
    evl(gate)
z_gates=[]
for gate in gates:
    if gate[0] == 'z':
        z_gates.append((gate,gates[gate][0]))
z_gates.sort(reverse=True)
print(int(''.join(list(map(lambda tup:str(tup[1]), z_gates))), 2))
