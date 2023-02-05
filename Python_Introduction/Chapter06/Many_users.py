users = {
    'a.einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'm.curie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
