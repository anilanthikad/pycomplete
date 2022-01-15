with open('csv_data.txt', 'r') as file:
    lines = file.readlines()
    file.close()

lines = [line.strip() for line in lines[1:]]

for line in lines:
    person_data = line.split(',')
    name = person_data[0]
    age = person_data[1].title()
    uni = person_data[2].capitalize()
    degree = person_data[3].title()

    print(f'{name} is {age} years old at {uni} and studying'
          f' {degree}.')

# =============================================================
# to put it back as csv file

sample_csv_value = ','.join(['Ralph', '25', 'MIT', 'CS'])
print(sample_csv_value)

