# Exercise - Birthday Dictionaries

birthdays = {
    "beyonce": "09/04/1981",
    "machine gun kelly": "04/22/1990",
    "jim parsons": "03/24/1973",
    "the ndertaker": "03/24/1965",
    "jennifer garner": "04/17/1972"
}

print("Welcome to the birthday dictionary. We know the birthdays of: ")
for name in birthdays:
    print(name)

print("Who's birthday do you want to look up? ")
name = input()

if name in birthdays:
    print("{}'s birthday is {}".format(name, birthdays[name]))
else:
    print("Unfortunately, we don't have {}'s birthday.".format(name))