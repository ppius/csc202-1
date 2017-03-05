#!/usr/bin/env python3
import time


def sum_of_n(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n+1):
        the_sum += i

    end = time.time()

    return the_sum, end - start


def sum_of_n2(n):
    start = time.time()

    the_sum = (n * (n + 1)) / 2

    end = time.time()

    return the_sum, end - start


def test_runtime(f):
    val = 10000
    for i in range(3):
        for i in range(5):
            print("Sum is {0} required {1} seconds".format(*f(val)))
        print()
        val *= 10


test_runtime(sum_of_n)
test_runtime(sum_of_n2)
