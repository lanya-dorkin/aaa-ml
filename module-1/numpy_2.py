import numpy as np


def solution():
    v = np.array(list(map(float, input().split())))
    n, t = input().split()
    n, t = int(n), float(t)

    us = np.array([input().split() for u in range(n)]).astype(float)

    squared_distances = np.power(us - v, 2)
    euclidian_distances = np.sqrt(np.sum(squared_distances, axis=1))

    indices = np.argwhere(euclidian_distances <= t).flatten()
    print(' '.join(map(str, indices)))


solution()
