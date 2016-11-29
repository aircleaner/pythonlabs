
def main():
    values = (1, 2, 3, 4, 3.14, [99, 98, 97], True, 'Hi')
    print(values)
    print(type(values))
    print(values[1])

    print(values[5])
    values[5][1] = 101
    print(values)
    values[5].append(999)
    print(values)

if __name__ == '__main__':
   main()