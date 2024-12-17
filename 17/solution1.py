#!/usr/bin/env pypy3

registers,program_=open(0).read().split('\n\n')
A_,B_,C_=registers.splitlines()
A: int=int(A_.split()[2])
B: int=int(B_.split()[2])
C: int=int(C_.split()[2])
program: list[int]=list(map(int,program_.split()[1].split(',')))
out=[]
IP=0

def halt(reason) -> None:
    global out
    print(f"Program halted because: {reason}. Output so far:")
    print(','.join(map(str,out)))
    raise SystemExit(1)

def combo(literal_operand: int) -> int:
    if 0 <= literal_operand <= 3:
        return literal_operand
    elif literal_operand == 4:
        return A
    elif literal_operand == 5:
        return B
    elif literal_operand == 6:
        return C
    elif literal_operand == 7:
        halt("combo operand 7")
    else:
        halt("combo operand invalid: " + str(literal_operand))

def fetch_execute():
    global program, A, B, C, IP
    if IP < 0 or IP >= len(program):
        halt("normal exit")
    if IP + 1 >= len(program):
        halt("operand index out of range: " + str(IP + 1))
    opcode = program[IP]
    operand = program[IP + 1]
    if opcode == 0: # adv
        A = A // 2 ** combo(operand)
    elif opcode == 1: # bxl
        B ^= operand
    elif opcode == 2: # bst
        B = combo(operand) & 7
    elif opcode == 3: # jnz
        if A != 0:
            IP = operand
            return
    elif opcode == 4: # bxc
        B ^= C
    elif opcode == 5: # out
        out.append(combo(operand) & 7)
    elif opcode == 6: # bdv
        B = A // 2 ** combo(operand)
    elif opcode == 7: # cdv
        C = A // 2 ** combo(operand)
    else:
        halt("invalid opcode: " + str(opcode))
    IP+=2

print(program)
while True:
    fetch_execute()
