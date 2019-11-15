#Encryption - Hackerrank

import math as m
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s.replace(" ", "")
    L=len(s)
    r=int(m.floor(m.sqrt(L)))
    c=int(m.ceil(m.sqrt(L)))
    if r*c < L:
        r=c

    li=[["" for j in range(c)] for i in range(r)]
    itr=0

    for i in range(r):
        for j in range(c):
            if itr< len(s) : 
                li[i][j]=s[itr]
            else:
                li[i][j]=' '
            itr+=1


    sres =""
    for j in range(c):
        for i in range(r):
            sres+=li[i][j]
        if sres[-1] != " ":
            sres+=" "
    return sres
          


s=raw_input()
print encryption(s)