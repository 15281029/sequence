import os
import sys
from collections import Iterable

sys.path.append(os.getcwd())
from sequence.tools import rander, timer


@timer
def shell(aiter):
    n = len(aiter)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if aiter[i] < aiter[i - gap]:
                    aiter[i], aiter[i - gap] = aiter[i - gap], aiter[i]
                    i -= gap
                else:
                    break
        gap //= 2


@timer
def insert(aiter):
    for i in range(len(aiter)-1):
        for j in range(i+1, len(aiter)):
            if aiter[i] > aiter[j]:
                temp = aiter[i]
                aiter[i] = aiter[j]
                aiter[j] = temp


@timer
def bubble(aiter):
    for passnum in range(len(aiter)-1, 0, -1):
        for i in range(passnum):
            if aiter[i] > aiter[i+1]:
                temp = aiter[i]
                aiter[i] = aiter[i+1]
                aiter[i+1] = temp


@timer
def selection(aiter):
    for i in range(len(aiter)-1, 0, -1):
        maxone = 0
        for j in range(1, i+1):
            if aiter[j] > aiter[maxone]:
                maxone = j
        temp = aiter[i]
        aiter[i] = aiter[maxone]
        aiter[maxone] = temp


rl = rander(quantity=20000, minval=0, maxval=100000, typed='di', repeat=False)
r1 = rl.randlist.copy()
r2 = rl.randlist.copy()
r3 = rl.randlist.copy()

shell(r1)
bubble(r2)
selection(r3)