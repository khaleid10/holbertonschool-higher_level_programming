#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0

    for num in set(my_list):
        total += num

    return total
