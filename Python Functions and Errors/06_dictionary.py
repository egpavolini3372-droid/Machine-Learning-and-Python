
import random
countries = ['colombia', 'mexico', 'argentina', 'peru']
population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

result= result = {country: population for (country, population) in population_v2.items() if population > 20}
print(result)

text = "Hola soy Erwin"
char_freq = {char: text.count(char) for char in text if char in 'aeiou'}
print(char_freq)

vocals = {c: c.upper() for c in text if c in 'aeiou'}
print(vocals)