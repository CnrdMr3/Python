def build_person(first_name, last_name, age):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name, 'age': age}
    return person

    if age:
        person['age'] = age


musician = build_person('jimi', 'hendrix', 27)
print(musician)
