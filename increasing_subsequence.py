# exercises on dynamic programming, increasing subsequence implementation
import random


# method for create random list with given length
def list_generator(size: int):
    return [random.randint(0,100) for _ in range(0, size)]


# method for create increasing subsequence
def increasing_subsequence(given_list):
    if not given_list:
        return None
    given_list_len = len(given_list)
    temporary_list = [1] * given_list_len

    # find maximal element and its index in maximal ordered subsequence
    for i in range(1, given_list_len):
        for j in range(0, i):
            if given_list[i] > given_list[j] and temporary_list[i] < temporary_list[j] + 1:
                temporary_list[i] = temporary_list[j] + 1
    max_len = max(temporary_list)
    max_index = temporary_list.index(max_len)
    result = [given_list[max_index]]
    current_len = max_len - 1

    # create maximal ordered subsequence
    for i in range(max_index - 1, -1, -1):
        if temporary_list[i] == current_len and given_list[i] < result[-1]:
            result.insert(0, given_list[i])
            current_len -= 1
    return result


# place of usage
if __name__ == "__main__":
    try:
        list_size = int(input('Define the length of the list:'))
        if list_size <= 0:
            raise ValueError("List size should be a positive integer.")

        random_list = list(list_generator(list_size))
        print("Original list:", random_list)

        maximal_ordered_subsequence = increasing_subsequence(random_list.copy())
        print("Maximal ordered subsequence:", maximal_ordered_subsequence)

    except ValueError as ve:
        print(f"Error: {ve}")
