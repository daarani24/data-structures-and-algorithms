import json

def duplicate(arr):
    n=len(arr)
    seen=set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False

arr=json.loads(input())
print(duplicate(arr))