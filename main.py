from a_perfect_number import print_numbers
from fast_and_reliable import stucture_search
from interleave import interleave
main_path= "resources/words.txt"

if __name__ == '__main__':

    # Function of the date 5.4.2
    print("Function of 5.4.2:result of Fast and reliable")
    with open(main_path, "r") as f:
        words_set = [], set
        main_list = [line.strip() for line in f]
        words_set = set(main_list)


    print("The list average search time ", stucture_search(main_list))
    print("The set average search time: ", stucture_search(main_list))



    # Function of the date 5.3
    print("Function of 5.3 , result of getting a perfect number:")
    print_numbers()
    print("\n")

    # Function of the date 5.4
    print("Function of 5.4:result of zipping the lists")
    for item in interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(item)
    print("\n")






