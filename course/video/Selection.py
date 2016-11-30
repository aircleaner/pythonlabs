
def main():
    name = input("What is your name? ")
    city = input("Where do you live?")
    if (name.lower() == "anna" or name.lower() == "jonas") and city.lower() == "bankekind":
        print("Wow, {0} is a great name! You live in {1}".format(name, city))
    else:
        print("Oh, hi", name)


if __name__ == '__main__':
   main()