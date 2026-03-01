s=input()
words=s.split()
r=[]
for i in words:
    r.append(i[::-1])
print(" ".join(r))