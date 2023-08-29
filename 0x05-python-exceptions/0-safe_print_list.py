#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    pr_num = 0
    try:
        while pr_num < x:
            print(my_list[pr_num], end='')
            pr_num += 1
    except IndexError:
        return pr_num
    finally:
        print()
    return pr_num


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
