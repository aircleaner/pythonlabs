
def main():
    pals = ['Peter', 'Anna', 'Jonas', 'Mikael', 'Anna']
    print(pals)
    print(pals[0])
    print(pals[1][2])
    pals.append('Lisa')
    print(pals)
    pals.remove('Anna')
    print(pals)
    pals.remove('Anna')
    print(pals)
    pals[0] = 'Anna'
    print(pals)
    print(type(pals))


if __name__ == '__main__':
   main()