
def my_range(n):
    return_list = []
    i = 0
    while i < n:
        return_list.append(i)
        i += 1
    return return_list


def my_new_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


def main():
    for i in my_new_range(1000000000000):
        print(i)


    g = my_new_range(3)
    print(type(g))
    print(g)
    print(next(g))
    print(next(g))
    print(next(g))
    #print(next(g))

if __name__ == '__main__':
    main()
