age = 33
price = 100

if age < 4:
    price = 0
elif age < 18:
    price = 0
elif age < 66:
    price = 50
elif age > 66:
    price = 75
print(f"Your admission cost is ${price}.")