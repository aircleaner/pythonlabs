import re


def main():
    phone = "ERD555-434-776!!"
    num = re.sub(r'\D', "", phone)  # r'' gives us a raw string
    print(num)

    test = "asdgfghj0704534532asdgj0704 34 23 19sdfhj0123456789sdafhgj"
    pattern = re.compile(r'07\d{8}')
    mobile_number = re.findall(pattern, test)
    print(mobile_number)
    pattern = re.compile(r'07\d{2}\D*\d{2}\D*\d{2}\D*\d{2}')
    mobile_number = re.findall(pattern, test)
    print(mobile_number)


if __name__ == '__main__':
    main()
