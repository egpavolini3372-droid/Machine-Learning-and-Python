
def filter_by_length(words):
   # Escribe tu solución
   new_list = list(filter(lambda x: len(x) >= 4, words))
   return new_list

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)