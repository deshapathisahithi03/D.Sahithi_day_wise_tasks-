# Creating an empty dictionary
d = {}
print(f"It is an empty dictionary: {d}")

# Creating a simple dictionary
d1 = {'spam': 2, 'eggs': 2}
print(f"The items are: {d1}")

# Creating a nested dictionary
d2 = {'food': {'ham': 1, 'egg': 2}}
print(f"The nested items are: {d2}")
print(f"Accessing the 'food' key in nested dictionary: {d2['food']}")

# Creating a dictionary using keyword arguments
d3 = dict(name='Bob', age=40)
print(f"The alternative construction is: {d3}")

# Creating a dictionary using zip
keys = ['bob', 'hi']
values = [50, 20]
d4 = dict(zip(keys, values))
print(f"The zipped dictionary is: {d4}")

# Creating a dictionary with `fromkeys`
d5 = dict.fromkeys(['a', 'b'])  # Without any values
print(f"The dictionary created with `fromkeys` is: {d5}")

# Accessing elements
# Uncommenting the following lines would raise KeyErrors because `d` is empty:
# d['eggs']
# d['food']['ham']

# Dictionary membership and methods
print(f"'eggs' in d: {'eggs' in d}")
print(f"Keys in d1: {list(d1.keys())}")
print(f"Values in d1: {list(d1.values())}")
