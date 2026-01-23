#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            try:
                div = a / b
            except ZeroDivisionError:
                print("division by 0")
                div = 0
            except TypeError:
                print("wrong type")
                div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return result
