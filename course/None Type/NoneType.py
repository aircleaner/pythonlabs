
def test_func(name, name_list=None):
    if not name_list:
        name_list = []
    name_list.append(name)
    print(name_list)


def main():
    x = None
    print(type(x))

    test_func("Anna")
    test_func("Peter")

    names = ["Erik"]
    test_func("Anna", names)
    test_func("Peter", names)


if __name__ == '__main__':
   main()
