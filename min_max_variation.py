#find the minimum unfairness for the possible subarray for the given array
#unfairness=max(_arr)-min(_arr), where _arr is the possible subarrays

import math
import os
import random
import re
import sys
from math import inf


def maxMin(k, arr):
    arr.sort()
    _min = inf
    start = 0
    stack = []
    for end, val in enumerate(arr):
        stack.append(val)
        if end - start + 1 == k:
            print(stack)
            unfairness = max(stack) - min(stack)
            if unfairness < _min:
                _min = unfairness
            stack.remove(arr[start])
            start += 1

    return _min


if __name__ == '__main__':

    n = 7

    k = 3

    arr = [10,100,300,200,1000,20,30]

    # for _ in range(n):
    #     arr_item = int(input().strip())
    #     arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)
