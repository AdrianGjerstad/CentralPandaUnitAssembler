import sys
import traceback

EXITS = [
    "0 Execution Success",
    "1 Unknown/Generic Error",
    "2 No Input File",
    "3 Unknown Option",
    "4 Invalid Option Format",
    "5 File Not Found"
]

TT_OPERATION = "OPERATION"
TT_REGISTER = "REGISTER"
TT_COMMA = "COMMA"

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if not self.value:
            return f'({self.type})'

        return f'({self.type}:{self.value})'

class Position:
    def __init__(self, idx, ln, col):
        self.idx = idx
        self.ln = ln
        self.col = col

    def advance(self, current_char):
        self.idx += 1

        self.col += 1
        if current_char == "\n":
            self.ln += 1
            self.col = 1

def assemble(data, output):
    # Lex tokens
    tokens = []
    pos = Position(1, 1, 1)

    for i in range(len(data)):
        current_char = data[i]

        if current_char == ",":
            tokens.append(Token(TT_COMMA))
            pos.advance(current_char)
        elif current_char in IDENT_START:
            tokens.append


def main(argc, argv):
    # Parse input arguments
    if argc < 2:
        return 2

    # Files to assemble
    files = []

    for i in range(1, argc):
        # Skip the file name of this file by going from 1
        if argv[i][0] == "-":
            # Single-Character Option
            if argv[i][1] == "-":
                # Double-Character Option
                return 3
            else:
                if len(argv[i]) > 2:
                    return 4

                return 3
        else:
            # Not an option
            files.append(argv[i])

    # Assemble files
    for i in range(len(files)):
        try:
            f = open(files[i], "rt")
        except FileNotFoundError:
            print("Could not open file: %s" % files[i])
            return 5

        # Assemble the file
        assemble(f.read(), files[i] + ".o")

    return 0 # Exit success

# DO NOT EDIT THE BELOW CODE.

if __name__ == "__main__":
    try:
        exit_code = main(len(sys.argv), sys.argv)
        if exit_code is None:
            exit_code = 1
        exit_text = EXITS[exit_code]
    except:
        sys.stderr.write("An error in the python code has occured.\n")
        sys.stderr.write("The information is below.\n\n")
        traceback.print_exc(file=sys.stderr)
        exit_code = 127
        exit_text = "127 Internal Error"

    print('\n%s' % (exit_text))

    sys.exit(exit_code)
