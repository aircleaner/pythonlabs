from functools import reduce


def get_max(a, b):
    if a > b:
        return a
    else:
        return b


def get_sum(a, b):
    return a + b


def main():
    list_of_number = [23, 143, 13, 4, 33, 9, 16, 97]

    max = reduce(get_max, list_of_number)
    sum = reduce(get_sum, list_of_number)

    max2 = reduce(lambda a, b: a if a > b else b, list_of_number)
    sum2 = reduce(lambda a, b: a + b, list_of_number)

    print(max)
    print(max2)
    print(sum)
    print(sum2)


if __name__ == '__main__':
    main()
