from datetime import date, datetime, timedelta
import random
from pprint import pprint
# from itertools import groupby
from functools import reduce
from typing import Callable, List, Dict

# TEMP
# print(date.today())

def random_date():
    return (date.today() - timedelta(days=random.randint(1, 3*365))).strftime('%d.%m.%Y')
    # return (date.today() - timedelta(days=random.randint(1, 3*365))

def random_num():
    return random.randint(5, 15)

# TEMP
# print(random_date())

array = []

def create_list_of_dicts():


    # TEMP
    i = 0
    print('\n\n')
    print("ARRAY-NICELY", end='\n\n')
        
    
    num = random_num()

    # TEMP:
    # print(f'num: {num}')

    while num > 0:


        id = random_num()
        created = random_date()
        title = 'array' + str(id)
        array.append({'id': id, 'created': created, 'title': title})

        # TEMP: print each dict in array
        print(array[i], sep='\n')
        i += 1

        num -= 1
    return array

array = create_list_of_dicts()

print('\n\n')
print("ARRAY", end='\n\n')
print(array)
print('\n\n')
pprint(array)
print('\n\n')

# Function to add item to dictionary if id is unique
def add_if_unique(accum, item):
    if item['id'] not in accum:
        accum[item['id']] = item
    return accum

# Reduce the array to a dictionary with unique ids
unique_dict = reduce(add_if_unique, array, {})

# Convert the dictionary back to a list
unique_array = list(unique_dict.values())

print("UNIQUE_ARRAY", end='\n\n')
print(unique_array)
print('\n\n')
pprint(unique_array)
print('\n\n')

# Function to sort the unique array by a provided key
def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

# Sort the unique_array by 'ID'
sorted_unique_array = sort_by_key(unique_array, 'id')

print("SORTED_UNIQUE_ARRAY", end='\n\n')
print(sorted_unique_array)
print('\n\n')
pprint(sorted_unique_array)
print('\n\n')


# Function to filter the unique array by a provided condition
def filter_by_condition(data: List[Dict], condition: Callable[[Dict], bool]) -> List[Dict]:
    return list(filter(condition, data))

# Example condition function
def example_condition(item: Dict) -> bool:
    return item['id'] == sorted_unique_array[0]['id']  # Example condition: ID == 0

# Filter the unique array by the example condition
filtered_unique_array = filter_by_condition(unique_array, example_condition)

print()
print("FILTERED_UNIQUE_ARRAY", end='\n\n')
print(filtered_unique_array)
print('\n\n')
pprint(filtered_unique_array)
print('\n\n')


# Transforming the list of dictionaries into a list of tuples
transformed_array = [(item['title'], item['id']) for item in unique_array]

print()
print("TRANSFORMED_ARRAY", end='\n\n')
print(transformed_array)
print('\n\n')
pprint(transformed_array)
print('\n\n')