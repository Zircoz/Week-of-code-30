n, t = map(int, input().split(' '))
c = input().split(' ')
for i in range(0, len(c)):
    c[i] = int(c[i])

b=0
inbowl = n
for i in range(t):
    if i+1 !=t:        
        inbowl=inbowl-c[i]
        if inbowl<5:
            b=b+n-inbowl
            inbowl=n
print(b)
