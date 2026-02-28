l=list(map(int,input().split()))
n=len(l)
flag=False
for i in range(n-1):
    if l[i]>l[i+1]:
        flag=False
        break
    else:
        flag=True
if flag==True:
    print("Sorted")
else:
    print("Not Sorted")