
from re import I


items =[
    {'product': 'shirt',
    'price':120},
    {'product': 'pants',
    'price':160},
    {'product': 'jacket',
    'price':205}
]

print(items)
prices = list(map(lambda i : i["price"], items))

print(prices)

def add_taxes(i):
    
    i["taxes"] = i["price"] * 0.19
    return i


new_items = list(map(add_taxes, items))
print(new_items)

