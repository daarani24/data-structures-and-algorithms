a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[]
i=0
j=0
while(i<len(a) and j<len(b)): 
    if(a[i]<=b[j]):
        l.append(a[i])
        i+=1
    else:
        l.append(b[j])
        j+=1
l.extend(a[i:])
l.extend(b[j:])
print(*l)