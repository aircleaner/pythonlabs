
def main():
    grade = input("Enter grade: ")
    grade = float(grade)

    letter_grade = ""
    if grade  >= 90.0:
        letter_grade = "A"
    elif grade >= 70.0:
        letter_grade = "B"
    elif grade >= 60.0:
        letter_grade = "C"
    elif grade >= 50.0:
        letter_grade = "D"
    elif grade >= 40.0:
        letter_grade = "E"
    else:
        letter_grade = "F"

    print("Your grade is: ", letter_grade)

if __name__ == '__main__':
   main()