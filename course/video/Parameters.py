
def say_hi(name, times = 1, end = "!"):
    for _ in range(times):
        print("Hi", name, end)

def main():
    say_hi("Jonas", 2)
    say_hi("Anna", 3)
    say_hi("Greta", end = "?")

if __name__ == '__main__':
   main()