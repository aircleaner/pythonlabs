
def main():
    my_list = ["John", "Sara", "Anna", "Peter"]
    for name in my_list:
        print("Hi", name)

    print("")

    name = "John-Paul"
    for c in name:
        print(c)

    print("")

    for i in range(10, 0, -2): # End is excluded
        print(i)

    print("")

    for _ in range(10):
        print("Hi")

    print("")

    my_friend = {"name": "John", "age": 26, "city": "London"}
    for k in my_friend:
        print(my_friend[k])

    for k,v in my_friend.items():
        print(k,"=",v)

if __name__ == '__main__':
   main()