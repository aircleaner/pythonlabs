
def main():
    person = {"name" : "John Smith", "age" : 37, "city" : "London"}
    print(person)
    print(person.keys())
    print(person.values())
    print(person["city"])
    person["country"] = "England"
    print(person)
    person["name"] = "Anne Jones"
    print(person)
    print(type(person))

if __name__ == '__main__':
   main()