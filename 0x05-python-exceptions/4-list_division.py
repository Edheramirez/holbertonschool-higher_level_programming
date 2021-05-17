#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = list()
    for i in range(list_length):
        try:
            currentValue = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            currentValue = 0
            print("division by 0")
        except TypeError:
            currentValue = 0
            print("wrong type")
        except IndexError:
            currentValue = 0
            print("out of range")
        finally:
            newlist.append(currentValue)
    return newlist
