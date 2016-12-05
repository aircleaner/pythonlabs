
def my_gen():
    for i in range(10):
        yield i**2


def main():
    gen = my_gen()
    print(type(gen))
    for x in gen:
        print(x)

    comp_gen = (i**2 for i in range(10))
    print(type(comp_gen))
    for x in comp_gen:
        print(x)

    text = "HI THERE"
    text_gen = (c.lower() for c in text)
    for c in text_gen:
        print(c)

    numbers = [3,6,4,6,8,9,10]
    comp_gen = (i**2 for i in numbers)
    for x in comp_gen:
        print(x)


if __name__ == '__main__':
    main()
