l=list(map(int,input().split()))
n=len(l)
k=int(input())
if k>n:
    k=k%n
print(*(l[k:]+ l[:k]))
