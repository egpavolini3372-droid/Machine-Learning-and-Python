
set_contries = {'Colombia', 'Mexico', 'Bolivia', 'Ecuador','Colombia'}

size= len(set_contries)
print("Size of the set:", size)

# Add more examples
print('Colombia' in set_contries)
set_contries.add('Peru')
print(set_contries)

# Updated examples
set_contries.update(['Argentina', 'Chile'])
print(set_contries)

# Remove an element
set_contries.remove('Bolivia')
print(set_contries)

set_contries.discard('Venezuela')  # No error if not found
print(set_contries)

set_contries.clear()
print(set_contries)