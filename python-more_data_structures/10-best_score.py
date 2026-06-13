#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_key = None
    best_value = 0

    for key, value in a_dictionary.items():
        if best_key is None or value > best_value:
            best_key = key
            best_value = value

    return best_key
