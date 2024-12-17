#!/usr/bin/env pypy3

registers,program_=open(0).read().split('\n\n')
A_,B_,C_=registers.splitlines()
A_init: int=int(A_.split()[2])
B_init: int=int(B_.split()[2])
C_init: int=int(C_.split()[2])
program: list[int]=list(map(int,program_.split()[1].split(',')))
rev_program = program[::-1]
out=[]
IP=0

def halt(reason) -> None:
    raise RuntimeError

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
    global program, A, B, C, IP, out
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
            return # FORGETTING TO PUT BACK THIS RETURN COST ME 2 HOURS OF TIME FFS AHAHAHAHH!!H!!11!1!
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

def get_sequence(a: int) -> list[int]:
    global program, A, B, C, IP, out
    A = a
    B = B_init
    C = C_init
    out=[]
    IP=0
    while True:
        try:
            fetch_execute()
        except KeyboardInterrupt:
            print("CPU panic")
            raise SystemExit(1)
        except RuntimeError:
            return out

def brute_force(a) -> int:
    for i in range(8):
        seq = get_sequence(a + i)[::-1]
        prefix=','.join(map(str, seq))
        entire_program=','.join(map(str, rev_program))
        prefix_match = entire_program.startswith(prefix)
        if not prefix_match:
            continue
        brute_force((a + i) * 8)
    print("Done")
    print("Value of A is        ", a // 8)
    print("Generated sequence is", prefix[:-2])
    print("Program is           ", entire_program)
    raise SystemExit(1)

print(brute_force(0))
