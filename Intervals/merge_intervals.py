def merge_interval(intervals):
    intervals.sort()
    res=[]
    for num in intervals:
        if not res or res[-1][1]<num[0]:
            res.append(num)
        else:
            res[-1][1]=max(res[-1][1],num[1])
    return res
n=int(input())
intervals=[]
for i in range(n):
    st,en=map(int,input().split())
    intervals.append([st,en])
res=merge_interval(intervals)
print(res)