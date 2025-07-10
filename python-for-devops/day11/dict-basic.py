# Basic
my_dict = {'name':'Maheen_Akhtar', 'age': 20, 'city': 'Islamabad'}

print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])

# Modifying and Adding Elements
my_dict['age'] = 24
my_dict ['city'] = 'Lalamusa'

print(my_dict['age'])
print(my_dict['city'])

# Removing
#del my_dict['city']
#print(my_dict)

# Checking key Existence
if 'age' in my_dict:
    print("Age is present in the dictionary")


# Iterating Through key and values
for value, key in my_dict.items():
    print(value, key)