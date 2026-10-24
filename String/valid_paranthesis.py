def isvalid(s):
    st=[]
    pairs={'}':'{',']':'[',')':'('}
    for ch in s:
        if ch in pairs:
            if not st or st[-1]!=pairs[ch]:
                return False
            st.pop()
        else:
            st.append(ch)
    return len(st)==0

s=input().strip()
if isvalid(s):
    print("True")
else:
    print("False")