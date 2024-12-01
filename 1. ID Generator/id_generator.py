# ID GENERATOR
from random import randint


print('** Unique ID Generator **')
name = input('Enter your name: ')
name_2 = name[0:2].upper()

surname = input('Enter your last name: ')
surname_2 = surname[0:2].upper()

year = input('Enter the year you were born: ')
year_2 = year[1:3]

# Generate random number
random = randint(1000,9999)

# ID Generated
id = f'{name_2}{surname_2}{year_2}{random}'

print(id)