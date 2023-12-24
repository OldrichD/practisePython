import timeit


def greatest_common_divisor_eucleid(a: int, b: int) -> int:
    higher_number = max(a, b)
    smaller_number = min(a, b)
    while True:
        remainder = higher_number % smaller_number
        if remainder == 0:
            break
        higher_number, smaller_number = smaller_number, remainder
    return abs(smaller_number)


def greatest_common_divisor_classic(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0

    divisor = min(abs(a), abs(b))

    while True:
        if a % divisor == 0 and b % divisor == 0:
            break
        divisor -= 1

    return abs(divisor)


if __name__ == "__main__":
    print('Welcome to Greatest Common Divisor (GCD) Finder!')

    try:
        number1 = int(input("Enter the first number:"))
        number2 = int(input("Enter the second number:"))

        common_divisor_classic_time = timeit.timeit(stmt=lambda: greatest_common_divisor_classic(number1, number2),
                                                    number=1000)
        common_divisor_classic = greatest_common_divisor_classic(number1, number2)
        common_divisor_eucleid_time = timeit.timeit(stmt=lambda: greatest_common_divisor_eucleid(number1, number2),
                                                    number=1000)
        common_divisor_eucleid = greatest_common_divisor_eucleid(number1, number2)

        if common_divisor_classic == 0:
            print(f'Both numbers {number1} and {number2} are zero. GCD is undefined.')
        elif common_divisor_classic == 1:
            print(f'Numbers {number1} and {number2} have no common divisor.')
        else:
            print(f'Greatest common divisor of {number1} and {number2} is {common_divisor_classic}, '
                  f'calculate by classic way in {common_divisor_classic_time}.')
            print(f'Greatest common divisor of {number1} and {number2} is {common_divisor_eucleid}, '
                  f'calculate by eucleid way in {common_divisor_eucleid_time}.')

    except ValueError as ve:
        print("Value error:", ve)
