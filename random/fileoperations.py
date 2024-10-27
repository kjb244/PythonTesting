import re
from pathlib import Path
from person import Person

path = Path(__file__).parent / "./data.txt"

file = open(path, 'r')
content = file.read().split('\n')
file.close()

content = content[1:]
people: [Person] = []

for item in content:
    name, age, dob = item.split('|')
    dob = re.sub(r"(\d{2})(\d{2})(\d+)", r"\1/\2/\3", dob)
    people.append(Person(name, age, dob))

