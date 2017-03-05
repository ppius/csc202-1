#!/usr/bin/env python3
import time


def sum_of_n_2(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n+1):
        the_sum += 1

    end = time.time()

    return the_sum, end - start


for i in range(10):
    print("Sum is {0} required {1} seconds".format(*sum_of_n_2(10000)))
