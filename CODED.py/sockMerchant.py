#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below. Hackerrank Problem
def sockMerchant(n, ar):
    x=n
    i=0
    cnt=0
    while i<x:
        j=i+1
        while j<x:
            if ar[i]==ar[j]:
                del ar[i]
                del ar[j-1]
                x=len(ar)
                i=-1
                j=i+2
                cnt+=1
                break
            j+=1
        i+=1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
