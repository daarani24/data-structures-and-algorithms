arr=list(map(int,input().split()))
target=int(input())
seen={}
for i,num in enumerate (arr):
    diff=target-num
    if diff in seen:
        print(seen[diff],i)
        break
    seen[num]=i
else:
    print('-1')