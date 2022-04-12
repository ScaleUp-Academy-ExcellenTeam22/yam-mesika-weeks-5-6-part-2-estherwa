from a_perfect_number import print_numbers
from interleave import interleave
if __name__ == '__main__':


    # Function of the date 5.3
    print("Function of 5.3 , result of getting a perfect number:")
    print_numbers()
    print("\n")

    print("Function of 5.4:result of zipping the lists")
    for item in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(item)
    print("\n")





