import sys
import getopt

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:")
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    input = None
    output = None
    for opt, arg in opts:
        if opt in ["-i"]:
            input = arg
        elif opt in ["-o"]:
            output = arg
        else:
            assert False, "unhandled option"

    if input == None:
        print("You must pass an input file with the flag -i")
    handle_files(input, output)


def to_bin(awas):
    if awas[0] != 'awa':
        sys.stderr.write("File does not start with an \'awa\'!\n")
        sys.exit(1)

    bin = ''
    for awa in awas[1:]:
        if awa == 'awa':
            bin += '0'
            continue
        bin += '0'
        was = int(len(awa[3:])/2)
        bin += '1' * was

    return bin


def handle_files(input, output):
    filename = input
    file = open(filename, 'r')
    if output == None:
        output = "output.bin"
    awas = file.read()
    awas = awas.split()
    output_file = open(output, 'w')
    output_file.write(to_bin(awas))


if __name__ == "__main__":
    main()
