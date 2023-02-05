# 5.3
alien_color = ['green', 'red', 'blue']
color = 'green'

if color in alien_color:
    print(f"You won 5 points")

# 5.4
alien_color = ['green', 'red', 'blue']
color = 'green'

for color in alien_color:
    if color == 'green':
        print("You have won 5 points.")
else:
    print("You won 10 points.")