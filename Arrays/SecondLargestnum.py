a=list(map(int,input().split()))
fl=sl=float("-inf")
for i in a:
  if (i>fl and i>sl):
    sl=fl
    fl=i
  elif (i>sl and i!=fl):
    sl=i
print(sl)
