
def main():
    name = "Peter \"''"
    print(name)
    print(name[0])
    age = "10"
    print(type(age))
    age = int(age) + 1
    print(age)
    print(type(age))
    age = str(age)
    print(type(age))

    #friend = "Bob"
    #friend[0] = "R"
    # str does not supprt item assignment
    #print(friend)


if __name__ == '__main__':
   main()