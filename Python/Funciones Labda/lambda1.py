
# people = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Cho", "house": "Ravenclaw"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# people.sort()

# print(people)

######

# people = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Cho", "house": "Ravenclaw"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# def f(person):
#     return person["name"]

# people.sort(key=f)

# print(people)

######

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)
