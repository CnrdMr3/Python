# 4.10(a)
message = "The first three items on the list are "
print(message)
places_to_visit = ['paris', 'berlin', 'venice', 'moskow', 'london', 'tokyo', 'athens']
message_0 = slice(0, 1, 2)
print(f"The first three items on the list are {places_to_visit[0:3]}.")

# 4.10(b)
message = "The first three items on the list are "
print(message)
places_to_visit = ['paris', 'berlin', 'venice', 'moskow', 'london', 'tokyo', 'athens']
message_0 = slice(0, 1, 2)
print(f"The first three items on the list are {places_to_visit[2:5]}.")

# 4.10(c)
message = "The first three items on the list are "
print(message)
places_to_visit = ['paris', 'berlin', 'venice', 'moskow', 'london', 'tokyo', 'athens']
message_0 = slice(0, 1, 2)
print(f"The first three items on the list are {places_to_visit[4:8]}.")

# 4.11
pizzas = ['Margerita', 'Feta&Spinach', 'Regina']
for pizza in pizzas:
    print(f"My favorite pizzas are {pizza.title()}.")

friends_pizza = ['Margerita', 'Feta&Spinach', 'Regina', 'Pepperoni']
for friend_pizza in friends_pizza:
    print(f"My friend's favorite pizzas are {friend_pizza.title()}.")