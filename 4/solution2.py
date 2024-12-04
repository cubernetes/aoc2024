#!/usr/bin/env python3

e=enumerate

data = open(0).read().strip().splitlines()

def find_x_mas(data: list[str], i: int, j: int) -> int:
    if i == 0 or i == len(data) - 1:
        return 0
    if j == 0 or j == len(data[0]) - 1:
        return 0
    diag1 = data[i - 1][j - 1] + data[i][j] + data[i + 1][j + 1]
    diag2 = data[i - 1][j + 1] + data[i][j] + data[i + 1][j - 1]
    if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
        return 1
    return 0

t = 0
for i, line in e(data):
    for j, c in e(line):
        t += find_x_mas(data, i, j)
print(t)
