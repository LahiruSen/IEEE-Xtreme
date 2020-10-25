import numpy as np

N, M, R, C = map(int, input().strip().split())
tile_configuration = []
for i in range(R):
    tile_configuration.append(list(map(int, input().strip().split())))

answer = 0
for i in range(R):
    for j in range(C):
        answer += tile_configuration[i][j]

a = N // R
b = M // C

print(answer * a * b)