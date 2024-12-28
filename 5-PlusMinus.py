#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    negative_num_count=0
    positive_num_count=0
    zero_count=0
    arr_len=len(arr)
    for n in arr:
        if n > 0:
            positive_num_count +=1
        elif n < 0:
            negative_num_count+=1
        elif n == 0:
            zero_count+=1
        else:
            print('Error interno')
    
    positive_ratio=positive_num_count/arr_len
    negative_ratio=negative_num_count/arr_len
    zero_ratio=zero_count/arr_len
    
    print(f'{positive_ratio:.6f}')
    print(f'{negative_ratio:.6f}')
    print(f'{zero_ratio:.6f}')
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
