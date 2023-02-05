# 3.8
places_to_visit = ['paris', 'berlin', 'venice', 'moskow', 'london']
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)

# 3.9
guest_list = ['Celeste', 'Ruan', 'Tian']
print(len(guest_list))

# 3.10
airplanes = ['Boeing', 'Airbus', 'Cessna']
print(airplanes)
message = f"Major airplane manufacturor {airplanes[0].title()}."
print(message)
airplanes.insert(3, 'Piper')
print(airplanes)
print(f"Major airplane manufacturor {airplanes[0]}.")
print(f"Major airplane manufacturor {airplanes[1]}.")
airplanes.insert(0, 'Lockheed-Martin')
print(airplanes)
airplanes.append('Mitsubishi')
print(airplanes)
popped_airplane = airplanes.pop()
print(airplanes)
print(popped_airplane)