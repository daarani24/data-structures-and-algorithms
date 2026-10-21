import json
stock=json.loads(input())
min_price=float('inf')
max_pro=0
for price in stock:
    if price<min_price:
        min_price=price
    else:
        cur=price-min_price
        if cur>max_pro:
            max_pro=cur
print(max_pro)