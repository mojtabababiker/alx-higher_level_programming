#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                new_list.append(my_list_1[i] / my_list_2[i])
            except (TypeError, ValueError):
                print("wrong type")
                new_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
    except IndexError:
        print("out of range")
    finally:
        for i in range(list_length - len(new_list)):
            new_list.append(0)
    return new_list


if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    my_l_1 = ['h']
    my_l_2 = [1, 2, 3, 4, 6, 7, 8]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
