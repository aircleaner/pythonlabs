
def my_func(*args):
    print("my_func with", len(args), "args")
    for value in args:
        print(value)


def my_func_2(**kwargs):
    print("my_func_2 with", len(kwargs), "kwargs")
    print(type(kwargs))
    print(kwargs)
    for k, v in kwargs.items():
        print(k, "=", v)


def my_func_3(*args, **kwargs):
    print("my_func_3 with", len(args), "args, and", len(kwargs), "kwargs")
    print("args:", args)
    print("kwargs:", kwargs)


def main():
    my_func(1, 3)
    my_func(2, 4, 6, 8)
    my_func(9)
    my_func()

    my_func_2(name="Jonas", age=28)
    my_func_2(city="London", country="UK", value=34)

    my_func_3(1, 2, 3, name="Jonas", age=28)
    my_func_3()
    my_func_3(animal="Dog")
    my_func_3(2, 3)


if __name__ == '__main__':
    main()
