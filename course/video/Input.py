
def main():
    name = input("What is your name? ")
    print("Hi", name)

    age = int(input("How old are you? ")) # This requires that the user inputs digits

    print("So you are {0} years old".format(age))

    age += 1
    print("{0} one year you will be {1} years old".format(name, age))


if __name__ == '__main__':
   main()