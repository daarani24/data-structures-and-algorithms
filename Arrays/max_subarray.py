import json
arr=json.loads(input())
cur=arr[0]
best=arr[0]
for i in arr[1:]:
    cur=max(i,cur+i)
    best=max(best,cur)
print(best)