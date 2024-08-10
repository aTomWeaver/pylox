import sys


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
    print("Running prompt")


def run(source):
    print(f"\"{source}\"")


if __name__ == "__main__":
    main()
