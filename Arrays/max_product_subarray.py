import json
arr=json.loads(input())
cur_max=cur_min=best=arr[0]
for i in arr[1:]:
    temp=(i,cur_max*i,cur_min*i)
    cur_max,cur_min=max(temp),min(temp)
    best=max(best,cur_max)
print(best)