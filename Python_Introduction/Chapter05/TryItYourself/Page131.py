# 5.1
dog = 'labrador'
dog == 'labrador'

print("Is dog == 'labrador'? I predict True.")
print(dog == 'labrador')

print("Is dog == 'poodle'? I predict False.")
print(dog == 'poodle')

print("Is dog == 'shitsiu'? I predict False.")
print(dog == 'shitsiu')

airplane = 'airbus'
airplane == 'airbus'

print("\nAirplane == 'airbus'. True")
print(airplane == 'airbus')

print("Airplane == 'boeing'. False")
print(airplane == 'boeing')

# 5.2
dog = 'Labrador'
dog == 'labrador'

print(dog == 'labrador')
print(dog.lower() == 'labrador')

age = 18
age == 18

print(age)

age_0 = 30
age_1 = 18

print(age_0 >= 18 or age_1 == 18)

# 5.3
dog_breed = ['labrador', 'poodle', 'bulldog']
dog = 'pit-bull'

if dog not in dog_breed:
    print(f"{dog.title()}, is not on the list.")