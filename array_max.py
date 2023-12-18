# find maximum of an array exercise

import random
from typing import List


# generator of array with given length with random int, str and float items
def random_array_generator(size: int):
    if size == 0:
        print("The input array should not be empty.")
    for item in range(size):
        yield random.randint(0, 99)


# method for find maximum in given array
def maximal_item(given_array: List[int]) -> int or None:
    if not given_array:
        return print("The input array is empty.")
    # return max(given_array)
    current_maximum = given_array[0]
    for item in given_array:
        if item > current_maximum:
            current_maximum = item
    return current_maximum


# place of usage
array = list(random_array_generator(10))
result = maximal_item(array)
print(f'Maximum in array {array} is item: {result}.')
