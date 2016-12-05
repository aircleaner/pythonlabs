
def main():
    with open("data.txt", "r") as f:
        print(f.read(6))
        print(f.read(2))
        print(f.tell())

        f.seek(25, 0)     # Move file counter to the second from the begining
        print(f.read(4))


if __name__ == '__main__':
    main()
