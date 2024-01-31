#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            print(my_list[i], end=' ')
            printed_elements += 1
    except IndexError:
        pass

    print()
    return printed_elements

my_list = [1, 2, 3, 4, 5]
num_printed = safe_print_list(my_list, 3)
print(f"Number of elements printed: {num_printed}")