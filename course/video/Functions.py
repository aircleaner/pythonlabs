
def print_it():
    print("Inside print_it() function")


def main():
    print("Starting main() function")
    print_it()
    print("Back from function call")
    print_it()
    print("Exiting main() function")

if __name__ == '__main__':
   main()