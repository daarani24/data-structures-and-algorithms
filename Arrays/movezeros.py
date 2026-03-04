def move_zeros(arr):
    n = len(arr)
    j = 0   
    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    while j < n:
        arr[j] = 0
        j += 1
    return arr
arr = list(map(int,input().split()))
print(move_zeros(arr))
