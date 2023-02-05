prompt = "Enter a number, and I'll tell you if it's even or odd: "
prompt += "\nEnter 'quit' to end the program. "
active = True

while active:
    number = input(prompt)

    if number == 'quit':
        active = False
    elif int(number) % 2 == 0:
        print(f"\nThe number {number} is even.")
    elif int(number) % 2 != 0:
        print(f"\nThe number {number} is odd.")