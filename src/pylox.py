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
    print(f"Running file: \"{path}\"")


def runPrompt():
    print("Running prompt")


if __name__ == "__main__":
    main()
