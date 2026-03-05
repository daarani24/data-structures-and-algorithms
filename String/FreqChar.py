a=input()
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
maxi=0
j=""
for i in d:
    if(maxi<d[i]):
        maxi=d[i]
        j=i
print(j,maxi)