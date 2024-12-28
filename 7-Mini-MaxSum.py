#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_number=0
    max_number=0
    arr.sort()
    largest_num=arr[-4:]
    smallest_num=arr[:4]
    
    for x,y in zip(largest_num,smallest_num):

        min_number+=y
        max_number+=x
        
    
    result= f"{min_number} {max_number}"
    return print(result)       
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
