import numpy as np


def solution():
    n, m, k = map(int, input().split())
    lines = [input().split() for line in range(m)]

    M = np.array([list(map(int, row)) for row in lines])

    max_sum = float('-inf')

    for up in range(0, m-n+1):
        for left in range(0, k-n+1):
            cur_sum = np.sum(M[up:up+n, left:left+n])
            max_sum = max(max_sum, cur_sum)

    print(str(int(max_sum)))


solution()
