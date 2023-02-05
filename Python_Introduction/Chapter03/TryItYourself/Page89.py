# 3.4
guest_list = ['Celeste', 'Ruan', 'Fred', 'Janke-Mari']
print(f"Kom braai en slaai {guest_list[0]}.")
print(f"Kom braai en slaai {guest_list[1]}.")
print(f"Kom braai en slaai {guest_list[2]}.")
print(f"Kom braai en slaai {guest_list[3]}.")

# 3.5
guest_list = ['Celeste', 'Ruan', 'Tian']
print(guest_list[2])
guest_list.remove('Tian')
guest_list.insert(2, 'Wilan')
print(guest_list)
print(f"Kom vir braai en slaai {guest_list[0]}")
print(f"Kom vir braai en slaai {guest_list[1]}")
print(f"Kom vir braai en slaai {guest_list[2]}")

# 3.6
guest_list = ['Celeste', 'Ruan', 'Tian']
guest_list.insert(0, 'Johan')
guest_list.insert(2, 'Xander')
guest_list.append('Pierre')
print(guest_list)

# 3.7
print(f"I can only take two people {guest_list[0]}.")
print(f"I can only take two people {guest_list[1]}.")
print(f"I can only take two people {guest_list[2]}.")
print(f"I can only take two people {guest_list[3]}.")
print(f"I can only take two people {guest_list[4]}.")
print(f"I can only take two people {guest_list[5]}.")
popped_guests = guest_list.pop()
print(guest_list)
print(popped_guest)