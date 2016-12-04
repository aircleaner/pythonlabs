
def main():
    # Creating
    word = "Hello World"

    # Accessing
    letter = word[0]
    print(letter)

    # Length
    print(len(word))

    # Counting
    s = "This is a string     with some spaces in it"
    print(s.count(" "))

    # Finding
    print(word.find("World"))

    # Slicing
    print(word[0])      # Prints the first char
    print(word[0:1])    # Start at 0 and take one char => Prints first char
    print(word[0:3])    # Prints the first 3 chars
    print(word[2:3])    # Prints index 2 (inclusive) and stop at index 3 (exclusive)
    print(word[:3])     # Same as 0:3
    print(word[-3:])    # Prints the last 3 chars
    print(word[3:])     # Prints from index 3 and to the end

    # Splitting
    s = "Pete;34;55;Main Street;US"
    fields = s.split(";")
    print(fields)
    print(type(fields))

    # Startswith/Endswith
    print(word.startswith("H"))
    print(word.endswith("d"))
    print(word.endswith("l"))

    # Repeating
    line = "_" * 80
    print(line)
    print(type(line))
    print(len(line))

    # Casing
    print(word.upper())
    print(word.lower())
    word2 = "hellO wOrld"
    print(word2.title())
    print(word2.capitalize())
    print(word2.swapcase())

    # Join
    result = "-".join(word)
    print(result)
    result = " ".join(word)
    print(result)
    result = word.join("--")
    print(result)

    # Concatinating
    result = word + "!"
    print(result)
    result = "Hi" + str(5)
    print(result)
    result = " ".join(["Hello", "World"])
    print(result)

    # Strip
    word2 = "     Hello World           "
    print("!" + word2 + "!")
    print("!" + word2.rstrip() + "!")
    print("!" + word2.lstrip() + "!")
    print("!" + word2.lstrip().rstrip() + "!")
    print("!" + word2.strip() + "!")

    # Testing content
    numword = "1356"
    print(numword.isdecimal())
    #age = ""
    #while not age.isdecimal():
    #    age = input("Input your age: ")
    #age = int(age)
    #print("Your age is:", age)

    print(word.isalpha())   # A space is not a letter
    print(numword.isalnum())
    print(word.isalnum())
    print(word.istitle())
    print(word.isupper())

    print("lo" in word)


if __name__ == '__main__':
   main()