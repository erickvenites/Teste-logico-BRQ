#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    count=""
    for i in range(n):
        count+="#"
        print(' '*(n-i-1)+count)
        
        
    #return print(count)    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
