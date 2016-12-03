
def main():
    my_list = [1, 2, 3, 4, 5]

    # List Comprehension
    result_list = [value**2 for value in my_list]
    print(type(result_list))
    print(result_list)

    # Set Comprehension
    result_set = {value**2 for value in my_list}
    print(type(result_set))
    print(result_set)

    # Dict Comprehension
    result_dict = {value: value**2 for value in my_list}
    print(type(result_dict))
    print(result_dict)

    # Tuple Comprehension
    result_tuple = (value**2 for value in my_list)
    print(type(result_tuple))
    print(result_tuple)
    # We cannot create a tuple this way :( This will create a generator instead
    result_tuple = tuple([value**2 for value in my_list]) # Use list (ordered) or set comprehension (unordered)
    print(type(result_tuple))
    print(result_tuple)

    # The same constructions as in the list comprehension can be used for all the other comprehensions.


if __name__ == '__main__':
   main()