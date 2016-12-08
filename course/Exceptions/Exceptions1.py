
def func(x, y):
    z = x / y
    print("Result of div:", z)
    return z


def main():
    try:
        result = func(10, 0)
    except ZeroDivisionError as e:
        print(e)
        # raise
    except FileExistsError or FileNotFoundError:
        pass
    else:
        print(result)
    finally:
        print("We will always end up here")

    print("Outside of try")

if __name__ == '__main__':
    main()
