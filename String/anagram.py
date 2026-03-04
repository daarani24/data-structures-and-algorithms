a=input().lower()
b=input().lower()
if(len(a)!=len(b)):
    print("Not Anagram")
a=sorted(a)
b=sorted(b)
if(a==b):
    print("Anagram")
else:
    print("Not Anagram") 
