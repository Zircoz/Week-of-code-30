#!/bin/python

import sys


n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
a = map(int, raw_input().strip().split(' '))
for a0 in xrange(q):
    left,right,x,y = raw_input().strip().split(' ')
    left,right,x,y = [int(left),int(right),int(x),int(y)]
    # your code goes here
    c=0
    for i in range(left,right+1):
        if y==a[i]%x:
            c=c+1
    print c
