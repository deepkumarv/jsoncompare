import json
import logging
import requests
from configparser import ConfigParser


# global declarations

# Function to compare Json
def compare_json_data(source_data_a, source_data_b):
    def compare(data_a, data_b):
        if type(data_a) is list:
            # is [data_b] a list and of same length as [data_a]?
            if (
                    (type(data_b) != list) or
                    (len(data_a) != len(data_b))
            ):
                print("(type(data_b) != list) or(len(data_a) != len(data_b))")
                return False

            # iterate over list items
            for list_index, list_item in enumerate(data_a):
                # compare [data_a] list item against [data_b] at index
                # print (list_index,list_item)
                # Adding now
                list_item_is_equal_to_list_item2 = False
                for list_index2, list_item2 in enumerate(data_b):

                    if (compare(list_item, list_item2)):
                        list_item_is_equal_to_list_item2 = True
                        break
                if (not list_item_is_equal_to_list_item2):
                    print("not list_item_is_equal_to_list_item2")
                    return False

                    # Till here
                # Commented below 2 lines
                # if (not compare(list_item, data_b[list_index])):
                #   return False

            # list identical
            return True

        # type: dictionary
        if type(data_a) is dict:
            # is [data_b] a dictionary?
            if type(data_b) != dict:
                print("type(data_b) != dict:")
                return False
            # print("dictionary")
            # iterate over dictionary keys
            for dict_key, dict_value in data_a.items():
                # print(dict_key,dict_value)
                # key exists in [data_b] dictionary, and same value?
                if (
                        (dict_key not in data_b) or
                        (not compare(dict_value, data_b[dict_key]))
                ):
                    print("(dict_key not in data_b) or(not compare(dict_value, data_b[dict_key]))"+" : "+ dict_key)
                    return False

            # dictionary identical
            return True

        # simple value - compare both value and type for equality
        return (
                (data_a == data_b) and
                (type(data_a) is type(data_b))
        )

    # compare a to b, then b to a
    return (
            compare(source_data_a, source_data_b) and
            compare(source_data_b, source_data_a)
    )


# Recursive function to sort the json (list or dictionary)
def ordered(obj):
    if (obj is None):
        print(obj)
        if isinstance(obj, dict):
            print("yes")
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        print(obj)
        return sorted(ordered(x) for x in obj if x != None)
    else:
        return obj


def main():
    file_a_object = open("A.json")
    file_b_object = open('B.json')
    A = json.load(file_a_object)
    B = json.load(file_b_object)
    is_equal = compare_json_data(A, B)
    if is_equal:
        print("Both are same")
    else:
        print("They are not equal")


if __name__ == "__main__":
    main()
