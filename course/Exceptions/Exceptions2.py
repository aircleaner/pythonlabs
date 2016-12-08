
def func(x, y):
    if y == 0:
        raise ValueError("Parameter y can NOT be zero")

    z = x / y

    print("Result of div:", z)
    return z


def main():
    try:
        result = func(10, 0)
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print(result)
    finally:
        print("We will always end up here")

    print("Outside of try")

if __name__ == '__main__':
    main()
