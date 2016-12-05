
def main():
    # https://en.wikipedia.org/wiki/List_of_file_signatures
    with open("arduino_debug.exe", "rb") as f:
        print(f.read(2))

    with open("image.gif", "rb") as f:
        print(f.read(6))

    with open("image.gif", "rb") as f:
        f.seek(13,0)
        for i in range(256):
            print(i, f.read(1).hex(), f.read(1).hex(), f.read(1).hex())

    with open("image.gif", "rb") as f_in:
        with open("image2.gif", "wb") as f_out:
            f_out.write(f_in.read(19))
            f_out.write(bytearray([255, 0, 0]))
            f_in.seek(19+3, 0)
            f_out.write(f_in.read())


if __name__ == '__main__':
    main()
