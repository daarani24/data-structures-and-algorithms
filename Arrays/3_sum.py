n=int(input())
arr=list(map(int,input().split()))
arr.sort()
res=[]
for i in range(n):
    if i>0 and arr[i]==arr[i-1]:
        continue
    l=i+1
    r=n-1
    while l<r:
        s=arr[i]+arr[l]+arr[r]
        if s==0:
            res.append([arr[i],arr[l],arr[r]])
            l+=1
            r-=1
            while l<r and arr[l]==arr[l-1]:
                l+=1
            while l<r and arr[r]==arr[r+1]:
                r-=1
        elif s<0:
            l+=1
        else:
            r-=1
print(res)