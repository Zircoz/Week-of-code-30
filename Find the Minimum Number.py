
import sys
def printminimum(k):
    if k==2:
        return 'min(int, int)'
    else:
        return 'min(int, ' + printminimum(k-1) + ')'


n = int(raw_input().strip())
print printminimum(n)
