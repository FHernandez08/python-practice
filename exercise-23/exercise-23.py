# Exercise - File Overlap

primenumbers = []
with open('exercise-23/primenumbers.txt') as prime_file:
    line = prime_file.readline()
    while line:
        line = line.strip()
        primenumbers.append(int(line))
        line = prime_file.readline()

happynumbers = []
with open('exercise-23/happynumbers.txt') as happy_file:
    line2 = happy_file.readline()
    while line2:
        line2 = line2.strip()
        happynumbers.append(int(line2))
        line2 = happy_file.readline()

overlapping_list = []

for x in primenumbers:
    if x in happynumbers:
        overlapping_list.append(x)

print(overlapping_list)