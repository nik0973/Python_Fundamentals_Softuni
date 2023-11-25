#1 create dictionary from scratch

# student = dict(name='Ivan', age=33, major='Computer Sciense')
# print(student)

#1.1 create dictionary from list with nested tuple
# student = dict([('name', 'Ivan'), ('age', 33), ('major', 'Computer Sciense')])
# print(student)

#1.2 create dictionary from list with nested tuple and list in tuple

# student = dict([('name', ['Ivan', 'Ivanov']), ('age', 33), ('major', 'Computer Sciense')])
# print(student)

#2 list to dictionary

# keys = ['name', 'age', 'major']
# values = ['Ivan', '33', 'Computer Sciense']
# student = {}
# for i in range(len(keys)):
#     key = keys[i]
#     value = values[i]
#     student[key] = value
# print(student)

# create dictionary from 2 list with zip function
# keys = ['name', 'age', 'major']
# values = ['Ivan', '33', 'Computer Sciense']
# student = dict(zip(keys, values))
#
# print(student)

# create dictionary from 2 list and nested list with zip function
# keys = ['name', 'age', 'major']
# values = [['Ivan', 'Dragan'], '33', 'Computer Sciense']
# student = dict(zip(keys, values))

# print(student)

# ^^^ Get value from list
# keys = ['name', 'age', 'major']
# values = ['Ivan', '33', 'Computer Sciense']
# student = dict(zip(keys, values))
#
# print(student['name'])  # Ivan
# print(student.get('name'))  # Ivan
# print(student.get('address'))   # None - when key is missing
# print(student['address'])   # KeyError - when key is missing

# Change value in Dictionary
# keys = ['name', 'age', 'major']
# values = ['Ivan', 33, 'Computer Sciense']
# student = dict(zip(keys, values))
# student['name'] = 'Dragan'
#
# print(student)
# print(student['name'])  # Dragan (changed value)

# Add additional pair to dictionary
# keys = ['name', 'age', 'major']
# values = ['Ivan', 33, 'Computer Sciense']
# student = dict(zip(keys, values))
# student['name'] = 'Dragan'
# student['phone'] = '+3598888888'
#
# print(student)
# print(student['name'])  # Dragan (changed value)
# print(student['phone']) # New pair

# Iterration by keys in dictionary
# squares = {1: 1, 2: 4, 3: 9}
# for key in squares.keys():
#     print(key, end=' ') # 1 2 3

# Iterration by keys and changed value
# squares = {1: 1, 2: 4, 3: 9}
# for key in squares.keys():
#     squares[key] *= 2
#     print(key, end=' ') # 1 2 3
#     print(squares)

#print values
# squares = {1: 1, 2: 4, 3: 9}
# for key in squares.values():
#     print(key, end=' ') # 1 4 9

#Iteration by values
# squares = {1: 1, 2: 4, 3: 9}
# for value in squares.values():
#     print(value, end=' ') # 1 4 9

# Use the keys to get the value
# squares = {1: 1, 2: 4, 3: 9}
# for key in squares.keys():
#     print(squares[key], end=' ') # 1 4 9

# Iteration by pair with items
# squares = {1: 1, 2: 4, 3: 9}
# for k, v in squares.items():
#     print('key', k)
#     print('value', v)

# Check for key in dict
# keys = ['name', 'age', 'major']
# values = ['Ivan', 33, 'Computer Sciense']
# student = dict(zip(keys, values))
# student['name'] = 'Dragan'
# student['phone'] = '+3598888888'

# if 'name' in student.keys():
#     print(student['name']) # Dragan
# check for value in dict
# if 'Dragan' in student.values():
#     print('update my dict') # update in my dict

#Clear the dict
# keys = ['name', 'age', 'major']
# values = ['Ivan', 33, 'Computer Sciense']
# student = dict(zip(keys, values))
# student['name'] = 'Dragan'
# student['phone'] = '+3598888888'
# student.clear()
# print(student)  # {}

# copy dict
# keys = ['name', 'age', 'major']
# values = ['Ivan', 33, 'Computer Sciense']
# student = dict(zip(keys, values))
# student['name'] = 'Dragan'
# student['phone'] = '+3598888888'
# student_copy = student.copy()
# print(student_copy) # same as student

# Metods in dict
#1.1 Pop
# app_configuration = {
#     'database_host': 'localhost',
#     'database_port': 3306,
#     'database_user': 'myuser',
#     'database_password': 'pass_example',
#     'database_name': 'sqlDB'
# }
# app_configuration.pop('database_host')
# print(app_configuration)

#1.2 popitem - removes the last pair
# app_configuration.popitem()
# print(app_configuration)

#1.3 Del - can del pair or whole dictionary
# del app_configuration['database_host'] # del only one pair
# del app_configuration # del whole dict
# print(app_configuration)

#1.3.1 Clear -  unlike del, clear remove values from dict but dict remain empthy
# app_configuration.clear()

#1.4 setdefault - add additional pair
# superuser = app_configuration.setdefault('superuser', 'mario123')
# print(superuser) # mario123
# print(app_configuration)

#1.5 update dict with value from another dict
# other_dict = {'superuser': '--MARIO--'}
# app_configuration.update(other_dict)
# print(app_configuration)

# Nested Dictionary
# student_records = {
#     'Ivan': {'Math': 5, 'Sciense': 6, 'English': 4},
#     'Nikolay': {'Math': 5, 'Sciense': 6, 'English': 4},
#     'Maria': {'Math': 5, 'Sciense': 6, 'English': 4}
# }
# Accessing an element
#print(student_records['Ivan']) # {'Math': 5, 'Sciense': 6, 'English': 4}
#print(student_records['Ivan']['Math']) # 5 - колкото вложени речници има, толкова квадратчета пишем – в случая 1 за 1 вложен речник
# adding an element
# student_records['Asia'] = {}    # 'Asia': {} - create new element in main dict with empthy nested dict
# student_records['Asia']['Iconomics'] = 4 # create element in nested dict for Asia
# student_records['Asia']['Math'] = 5 # create second element in nested dict for Asia etc.
# print(student_records)

# Iterate trough nested dictionary - use nested for-loops
# shopping_list = {
#     "foods": {"nuts": "almonds"},
#     "drinks": {"soft": "lemonade", "wine": "merlot"}
# }
# for key, value in shopping_list.items():
#     for nested_key, nested_value in value.items():
#         print(f'{nested_value} bought')
#         shopping_list[key][nested_key] = 'bought'

# student_records = {
#     'Ivan': {'Math': 5, 'Sciense': 6, 'English': 4},
#     'Nikolay': {'Math': 5, 'Sciense': 6, 'English': 4},
#     'Maria': {'Math': 5, 'Sciense': 6, 'English': 4}
# }
# for name, value in student_records.items():
#     print(f'***{name}***')
#     for n_name, n_value in value.items():
#         print(f'{n_name} - {n_value}', end='; ')
#     print()

# Dictionary comprehensions
# data = [('Peter', 22), ('Amy', 18), ('George', 35)]
# dictionary = {key:value for (key, value) in data}
# print(dictionary)

# nums = [1, 2, 3]
# cubes = {num:num ** 3 for num in nums}
# print(cubes)