# implementation of selection sort method exercise

import random
from typing import List


# generator of the list with float elements (-100, 100)

# def float_list_generator(size: int):
#     for _ in range(size):
#         yield round(random.uniform(0, 100), 1)

def float_list_generator(size: int) -> List[float]:
    return [round(random.uniform(0, 100), 1) for _ in range(size)]


def selection_sort(given_list):
    list_len = len(given_list)
    for i in range(0, list_len):
        min_item = min(given_list[i:])
        index_item = given_list.index(min_item)
        given_list[i], given_list[index_item] = min_item, given_list[i]
    return given_list


# place of usage
if __name__ == "__main__":
    try:
        list_size = int(input('Define the length of the list:'))
        if list_size <= 0:
            raise ValueError("List size should be a positive integer.")

        list_to_sort = list(float_list_generator(list_size))
        print("Original List:", list_to_sort)

        sorted_list = selection_sort(list_to_sort.copy())
        print("Sorted List:", sorted_list)

    except ValueError as ve:
        print(f"Error: {ve}")
