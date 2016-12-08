
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("base", type=int, help="The base")
    parser.add_argument("exponent", type=int, help="The exponent")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase putput verbosity")
    return parser.parse_args()


def main():
    args = parse_arguments()

    answer = args.base**args.exponent
    if args.verbose >= 2:
        print("The square of {} equals {}".format(args.base, answer))
    elif args.verbose == 1:
        print("{}^2={}".format(args.base, answer))
    else:
        print(answer)


if __name__ == '__main__':
    main()
