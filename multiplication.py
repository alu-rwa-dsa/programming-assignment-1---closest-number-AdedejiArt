import math
import os
import random
import re
import sys


# Complete the closestNumbers function below.
def closestNumbers(arr):
    output = []
    arr = sorted(arr)
    current_min = 10 ** 9
    for i in range(1, len(arr)):
        difference = abs(arr[i - 1] - arr[i])

        if difference < current_min:
            output = [(arr[i - 1], arr[i])]
            current_min = difference

        elif difference == current_min:
            output.append((arr[i - 1], arr[i]))

    flat_list = [i for sublist in output for i in sublist]
    return flat_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()










