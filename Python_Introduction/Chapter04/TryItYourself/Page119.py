# 4.13
five_foods = ("bread", "apple", "banana", "orange", "cheese")
for food in five_foods:
    print(f"{food.title()}.")

# 4.13(b)
five_foods = ("\nmango", "apple", "banana", "orange", "cheese")
print(five_foods[0])
print(five_foods[1])
print(five_foods[2])
print(five_foods[3])
print(five_foods[4])

five_foods = ("\nbread", "apple", "banana", "orange", "cheese")
for food in five_foods:
    print(f"{food.title()}.")

revised_foods = ("bread", "oats", "banana", "fish", "cheese")
for other_foods in revised_foods:
    print(f"\n{other_foods.title()}.")