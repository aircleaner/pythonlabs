
def main():
    my_list = [1, 2, 3, 4, 5]

    result_list = []
    for value in my_list:
        result_list.append(value**2)
    print(result_list)

    result_list_2 = [value**2 for value in my_list]
    print(result_list_2)

    result_list_3 = []
    for value in my_list:
        if value != 3:
            result_list_3.append(value**2)
    print(result_list_3)

    result_list_4 = [value**2 for value in my_list if value != 3]
    print(result_list_4)

    result_list_5 = []
    for value in my_list:
        if value != 3:
            result_list_5.append(value**2)
        else:
            result_list_5.append((value**3))
    print(result_list_5)

    result_list_6 = [value**2 if value != 3 else value**3 for value in my_list]
    print(result_list_6)

    result_list_7 = [i*j for i in range(4) for j in range(3)]
    print(result_list_7)

    result_list_8 = []
    for i in range(4):
        for j in range(3):
            result_list_8.append(i*j)
    print(result_list_8)


if __name__ == '__main__':
   main()