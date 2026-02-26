arr=list(map(int,input().split()))
l=[]
for i in arr:
  if i not in l:
    l.append(i)
print(l)
