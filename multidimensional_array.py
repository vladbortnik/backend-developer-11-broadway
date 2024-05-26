from datetime import date, datetime, timedelta
import random
from pprint import pprint
from functools import reduce
from typing import Callable, List, Dict

def random_date():
    return (date.today() - timedelta(days=random.randint(1, 3*365))).strftime('%d.%m.%Y')

def random_num():
    return random.randint(5, 20)

array = []

def create_list_of_dicts():
    
    num = random_num()
    while num > 0:
        id = random_num()
        created = random_date()
        title = 'array' + str(id)
        array.append({'id': id, 'created': created, 'title': title})
        num -= 1
    return array

# A service function to be used in reduce()
def add_if_unique(accum, item):
    if item['id'] not in accum:
        accum[item['id']] = item
    return accum

# Sorts the 'unique_array' (aka list_of_dicts) by a provided key
def sort_by_key(data, key):
    return sorted(data, key=lambda x: x[key])

# Function to filter the 'unique_array' by a provided condition
def filter_by_condition(data: List[Dict], condition: Callable[[Dict], bool]) -> List[Dict]:
    return list(filter(condition, data))

# A service func to be used with 'filter_by_condition()'
# Makes it easy to filter the 'unique_array' by any 'key'
def example_condition(item: Dict) -> bool:
    # To make sure the 'example_condition' evaluates to 'True' 
    # the 1st element of the 'sorted_unique_array' is used -> (index == 0)
    return item['id'] == sorted_unique_array[0]['id']  # Example condition: sort by 'id'

if __name__ == '__main__':

    array = create_list_of_dicts()
    pprint(array)
    print()

    # Reduce() is used to avoid explicit loops
    unique_dict = reduce(add_if_unique, array, {})

    # Parses the initial 'array' and illuminates duplicates
    unique_array = list(unique_dict.values())
    pprint(unique_array)
    print()

    # Sorts the 'unique_array' by 'IDs'
    sorted_unique_array = sort_by_key(unique_array, 'id')
    pprint(sorted_unique_array)
    print()

    # Filters the 'unique_array' by the 'example_condition'
    filtered_unique_array = filter_by_condition(unique_array, example_condition)
    pprint(filtered_unique_array)
    print()

    # Transforming the list of dictionaries into a list of tuples
    transformed_array = [(item['title'], item['id']) for item in unique_array]
    pprint(transformed_array)
    print()
    