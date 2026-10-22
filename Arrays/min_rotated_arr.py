def rotate(arr):
    n=len(arr)
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid
    return arr[low]
import json
arr=json.loads(input())
print(rotate(arr))