import random
dictionary = {}

for i in range(1,11):
    dictionary[i] = i * 2

print(dictionary)
print(type(dictionary))

dictionary_v2 = {i: i * 2 for i in range(1, 11)}
print(dictionary_v2)

countries = ['colombia', 'mexico', 'argentina', 'peru']
print(type(countries))
population = {}
for country in countries:
    population[country] = random.randint(1, 100)

print(population)   

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

names = ['Ana', 'Luis', 'Carlos', 'Maria']
ages = [23, 34, 45, 22]

names_ages = {}
for i in range(len(names)):
    names_ages[names[i]] = ages[i] 
print(names_ages)
names_ages_v2 = {names[i]: ages[i] for i in range(len(names))} 
print(names_ages_v2)

print(list(zip(names, ages)))
new_dict = {name: age for name, age in zip(names, ages)}
print(new_dict)