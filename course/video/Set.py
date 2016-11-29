
def main():
    my_set = {1, 2, 3}
    print(type(my_set))
    print(my_set)
    my_set.add(4)
    print(my_set)
    my_set.add(2)
    print(my_set)

    my_list =[1, 2, 3, 1, 2, 3, 1, 1]
    print(my_list)
    print(set(my_list))
    print(list(set(my_list)))

    my_other_set = {1, 3, 5, 7}
    print(my_set.intersection(my_other_set))


if __name__ == '__main__':
   main()