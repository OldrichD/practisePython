# implementation of bubble-sort method exercise

import random
from typing import List


# generator of the list with float elements (-100, 100)

# def float_list_generator(size: int):
#     for _ in range(size):
#         yield round(random.uniform(0, 100), 1)

def float_list_generator(size: int) -> List[float]:
    return [round(random.uniform(0, 100), 1) for _ in range(size)]


# implementation of bubble-sort method
def bubble_sort(given_list):
    list_len = len(given_list)
    change = True
    # while change:
    for _ in range(list_len):
        change = False
        for i in range(0, list_len-1):
            if given_list[i] > given_list[i+1]:
                # copy_element = given_list[i]
                # given_list[i] = given_list[i+1]
                # given_list[i+1] = copy_element
                given_list[i], given_list[i + 1] = given_list[i + 1], given_list[i]
                change = True
        if not change:
            break
    return given_list


# place of usage
if __name__ == "__main__":
    try:
        list_size = int(input('Define the length of the list:'))
        if list_size <= 0:
            raise ValueError("List size should be a positive integer.")

        list_to_sort = list(float_list_generator(list_size))
        print("Original List:", list_to_sort)

        sorted_list = bubble_sort(list_to_sort.copy())
        print("Sorted List:", sorted_list)

    except ValueError as ve:
        print(f"Error: {ve}")






