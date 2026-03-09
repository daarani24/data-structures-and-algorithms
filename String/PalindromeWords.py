def palin(s):
    for i in s:
        if i==i[::-1]:
            print(i,end=" ")
s=input().split()
a=(palin(s))