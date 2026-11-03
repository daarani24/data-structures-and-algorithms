def contains_water(arr):
    l,r=0,len(arr)-1
    max_area=0
    while l<r:
        h=min(arr[l],arr[r])
        w=r-l
        max_area=max(max_area,h*w)
        if arr[l]<arr[r]:
            l+=1
        else:
            r-=1
    return max_area
arr=list(map(int,input().split()))
print(contains_water(arr))