import add_module
from add_module import add
from add_module import add as a_func
#from add_module import *   # import all functions from add_module, avoid this type of import


def add(a, b):
    return "Haha"


def main():
    x = add_module.add(3, 4)    # Uses import add_module
    print(x)

    y = add(1, 3)   # Uses from add_module import add, conflict with local add
    print(y)
    z = a_func(5,6)
    print(z)    # Uses from add_module import add as a_func


if __name__ == '__main__':
    main()
