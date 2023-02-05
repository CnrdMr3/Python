favorite_foods = {
    'German': ['sauerkraut', 'kartofelen'],
    'French': ['Foodie-foods'],
    'USA': ['Burgers', 'Subway'],
    'Russians': ['Cabbage-soup', 'Potatoes']
}

for name, foods in favorite_foods.items():
    print(f"\n{name.title()}'s favorite foods are:")

    for food in foods:
        print(f"\t{food.title()}")