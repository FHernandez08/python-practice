# Exercise - Read from file

dict_counter = {}

with open('exercise-22/nameslist.txt') as names:
    line = names.readline()

    while line:
        line = line.strip()
        if line in dict_counter:
            dict_counter[line] += 1
        else:
            dict_counter[line] = 1
        line = names.readline()

print(dict_counter)