import sys
from scanner import Scanner


def main():
    args = sys.argv[1:]
    if len(args) > 1:
        print("Usage: pylox: [script]")
        sys.exit(64)
    elif (len(args) == 1):
        runFile(args[0])
    else:
        runPrompt()


def runFile(path):
    with open(path, 'r') as sourcefile:
        source = sourcefile.read()
    run(source)


def runPrompt():
    while True:
        line = input("> ")
        if line == "exit()":  # TODO: proper EOF detection
            break
        run(line)


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scanTokens()

    for token in tokens:
        print(token)


if __name__ == "__main__":
    main()
