
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "The name is " + self.name + " and the age is " + str(self.age)

    # __del__ is called automatically
    def __del__(self):
        print(self.name, "is dead")

    def print_name(self):
        print(self.name)


class Employee(Person):
    def __init__(self, name, age, emp_no):
        super().__init__(name, age)
        self.emp_no = emp_no

    def __str__(self):
        return "Employee " + self.name + " has employee number: " + self.emp_no

    def work(self):
        print(self.name + " is working")

def my_func():
    p = Person("John", 14)


def main():
    p1 = Person("Sue", 25)
    p2 = Person("Bob", 34)
    my_func()
    print(p1.name)
    print(p2.name)

    p1.print_name()
    p2.print_name()

    print(p1.__str__())
    print(p2.__str__())

    e1 = Employee("John", 44, "12344")
    print(e1)
    e1.work()
    e1.print_name()

    emp_list = []
    for i in range(100):
        e = Employee(str(i), i, str(i))
        emp_list.append(e)

    for emp in emp_list:
        print(emp)


if __name__ == '__main__':
    main()
