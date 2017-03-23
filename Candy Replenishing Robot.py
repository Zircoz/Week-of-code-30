import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
c = map(int, raw_input().strip().split(' '))
# your code goes here
b=0
bowl=n
for i in range(t):
    if i+1 !=t:
        
        bowl=bowl-c[i]
        if bowl<5:
            b=b+n-bowl
            bowl=n
print b
