import json

birthdays = {
    "beyonce": "09/04/1981",
    "machine gun kelly": "04/22/1990",
    "jim parsons": "03/24/1973",
    "the ndertaker": "03/24/1965",
    "jennifer garner": "04/17/1972"
}

with open('birthdays.json', 'r') as fout:
    json.dump(birthdays, fout)

while True:
    birthday = input("Who's birthday do you want to look up? ")
    with open('birthdays.json', 'r') as fin:
        info = json.load(fin)

    if birthday in info:
        print(f"{birthday}'s birthday is {birthdays.get(birthday)}")
    else:
        print(f"{birthday}'s birthday is not in the file")