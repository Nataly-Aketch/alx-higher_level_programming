#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list3 = []

    for i in range(list_length):
        for j in range(list_length):
            try:
                if i == j:
                    result = my_list_1[i]/my_list_2[j]
                    list3 += [result]
            except ZeroDivisionError:
                print("division by 0")
                list3 += [0]
            except TypeError:
                print("wrong type")
                list3 += [0]
            except IndexError:
                print("out of range")
                list3 += [0]
            finally:
                pass
    return list3
