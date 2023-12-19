# exercise on factorial implementation

import timeit


# calculation of factorial using the for loop
def factorial_loop(n: int) -> int or None:
    if n < 0:
        return None
    step = 1
    for i in range(1, n+1):
        step *= i
    return step


# calculation of factorial using the recursion
def factorial_recursion(n: int) -> int or None:
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)


# place of usage
entry_n = int(input("Define the n for the calculation of its factorial:"))

# Measurement using timeit for factorial_loop
factorial_loop_time = timeit.timeit(stmt=lambda: factorial_loop(entry_n), number=1000) / 1000

result = factorial_loop(entry_n)
if result is None:
    print(f'Factorial of {entry_n} is not defined.')
else:
    print(f'Factorial (count with loop) of {entry_n} is {result}. (calculate in {factorial_loop_time} s)')

# Measurement using timeit for factorial_recursion
factorial_recursion_time = timeit.timeit(stmt=lambda: factorial_recursion(entry_n), number=1000) / 1000

result = factorial_recursion(entry_n)
if result is None:
    print(f'Factorial of {entry_n} is not defined.')
else:
    print(f'Factorial (count with recursion) of {entry_n} is {result}. (calculate in {factorial_recursion_time} s)')