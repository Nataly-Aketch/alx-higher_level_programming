#/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        count2 = 0
        for i in my_list:
            count += 1
        if x >= count:
            raise IndexError
    except IndexError:
        for j in range(count):
            print(my_list[j], end="")
            count2 += 1
        print(end="\n")
    else:
        for j in range(x):
            print(my_list[j], end="")
            count2 += 1
        print(end="\n")
    return count2
