
def add(a, b):
    return a + b

def greeting(name, times):
    greeting_str = ""
    for _ in range(times):
        greeting_str += "Hi " + name + "\n"
    return greeting_str

def return_values(a, b):
    return a * 2, b * 3, a * b

def main():
    x = add(2, 3)
    print(x)

    ret_str = greeting("Jonas", 3)
    print(ret_str, end="")

    ret_str = greeting("Anna", 5)
    print(ret_str, end="")

    y = return_values(4, 5)
    print(y)

    a,b,c = return_values(4, 5)
    print(a)
    print(b)
    print(c)


if __name__ == '__main__':
   main()