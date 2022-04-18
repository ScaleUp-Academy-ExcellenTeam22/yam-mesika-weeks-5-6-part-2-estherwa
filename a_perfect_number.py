from typing import Generator


def create_perfect_numbers() -> Generator:
    """
    Function that generates perfect numbers that  is a positive integer that is
    equal to the sum of its positive divisors, excluding the number itself.
    :return: A generator of the number that is perfect.
    """
    current_num = 1
    div_sum = 0
    divider = 0
    while True:
        while current_num > divider:
            for divider in range(1, int(current_num / 2) + 1):
                if current_num % divider == 0:
                    div_sum += divider
                else:
                    divider += 1

            if div_sum == current_num:
                yield current_num
            div_sum = 0
            current_num += 1

        divider = 2


def main_function():
    """
    Function that calls the main one and prints the list of all the perfect numbers.
    """
    generator = create_perfect_numbers()
    while True:
        print(next(generator))
