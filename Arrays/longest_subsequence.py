def subsequence(x,y):
    res=0
    n=len(y)
    for i in range(n):
        j=i
        for ch in x:
            if j<n and ch==y[j]:
                j+=1
        res=max(res,j-i)
    return res
s1=input()
s2=input()
print(subsequence(s1,s2))