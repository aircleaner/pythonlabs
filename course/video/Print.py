
def main():
    x = 10
    print(x)

    print("Hi there")

    print("Hi there", x)

    name = "John"
    print("Hi there", name)

    print("This is", name, "'s bike")
    print("This is", name, "'s bike", sep="")

    print("This is {0}'s bike".format(name))
    age = 17

    print("Hi", end="->")
    print("Bye")

    print("This is {0}'s bike. He is {1} years old. Bye {0}!".format(name, age))

    # Not in video
    print("This is %s's bike" % name)


if __name__ == '__main__':
   main()