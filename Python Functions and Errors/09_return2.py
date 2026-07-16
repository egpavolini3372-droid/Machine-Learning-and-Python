
def find_volume(length, width, height):
    volume = length * width * height, "cm3", "width=" + str(width)
    return volume
v = find_volume(2, 3, 4)

volume, unit, width_info = find_volume(2, 3, 4)
print(volume)  # Output: 24
print(unit)    # Output: cm3
print(width_info)  # Output: width=3
print(v)  # Output: 24 cm3 width=3