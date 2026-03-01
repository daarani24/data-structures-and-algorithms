n=int(input())
arr=list(map(int,input().split()))
tot_sum=n*(n+1)//2
arr_sum=sum(arr)
miss_val=tot_sum-arr_sum
print(miss_val)