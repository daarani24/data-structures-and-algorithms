import json
arr=json.loads(input())
n=len(arr)
ans=[1]*n
pre=1
for i in range(n):
    ans[i]=pre
    pre*=arr[i]
suf=1
for i in range(n-1,-1,-1):
    ans[i]*=suf
    suf*=arr[i]
print(ans)
