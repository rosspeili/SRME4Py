#here you can find a list of simple random program examples
#make sure you follow the aesthetic and be explanatory ;)

#import random module

import random

#run this program to generate a random decimal number between 0 and 1

value1 = random.random()
print(value1)

#run this program to generate a random decimal number between 1 and 10

value2 = random.uniform(1, 10)
print(value2)

#run this program to generate a random natural number between 1 and 10

value3 = random.randint(1, 10)
print(value3)

#run this program to find out who's washing the dishes tonight!

participants = ['Akis', 'Rafas', 'Vlad']
value4 = random.choice(participants)
print(value4 + ' is going to wash the dishes tonight!')

#run this program to randomly distribute 10 equal items to 3 subjects

subjects = ['Jorge', 'Pim', 'Nathan']
value5 = random.choices(subjects, k=10)
print(value5)

#run this program to randomly distribute 10 equal items to 3 subjects with a % rate for each subject
#50, 30, 20 are the picking rate for Jorge, Pim, Nathan respectively

value6 = random.choices(subjects, weights=[50, 30, 20], k=10)
print(value6)

#run this program to randomly shuffle a list, then pick 3 random unique numbers out of the list

value7 = list(range(1, 10))
random.shuffle(value7)
print(value7)

value8 = random.sample(value7, k=3)
print(value8)

#run this program to randomly generate 2 fake subject based on the given information

firstnames = ['John', 'Elrich', 'Givi', 'Tamara', 'Lasha', 'Federico', 'Anna', 'Fabio', 'Tato', 'Samuel']
lastnames = ['Palmer', 'Havock', 'Johnson', 'Zinewski', 'Aguilar', 'Soselia', 'Muti', 'Ibente', 'Nagoa', 'Pose']
citynames = ['Santa Clara', 'Illinois', 'Delft', 'Zuug', 'Thessaloniki', 'Osaka', 'Liubliana', 'Dubai', 'London', 'Moscow']
occupation = ['Venture Capitalist', 'Reproductive Technologies Researcher', 'IT Security Specialist', 'Software Developer', 'Architect', 'Mechanical Engineer', 'Unemployed', 'Logistics Manager', 'Fusion Energy Scientist']

for num in range(2):
    first = random.choice(firstnames)
    last = random.choice(lastnames)
    city = random.choice(citynames)
    work = random.choice(occupation)

    print(f'{first} {last}\n{city}\n{work}\n')

#run this program to create a random phone number for the city of Thessaloniki

phone = f'{2310}-{random.randint(100, 999)}-{random.randint(100, 999)}'
print(phone)

#
