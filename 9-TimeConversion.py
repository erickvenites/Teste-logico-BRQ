#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    newHour=""
    aux=0
    
    if s[-2:]== "PM":
        aux=int(s[0:2])
        
        if aux !=12:
            aux+=12
            
        newHour=s.replace(s[0:2],str(aux))
        newHour=newHour.replace("PM","")
        
    elif s[-2:]=="AM":
        newHour=s[0:8]
        
        if newHour[0:2]=="12":
            newHour=newHour.replace("12","00")
    else: 
        print("Error ao formatar a  hora")
    
    
    return newHour
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
