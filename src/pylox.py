import sys
from scanner import Scanner


class Lox:
    def __init__(self):
        self.hadError = False

    def main(self):
        args = sys.argv[1:]
        if len(args) > 1:
            print("Usage: pylox: [script]")
            sys.exit(64)
        elif (len(args) == 1):
            self.runFile(args[0])
        else:
            self.runPrompt()

    def runFile(self, path: str):
        with open(path, 'r') as sourcefile:
            source = sourcefile.read()
        self.run(source)
        if self.hadError:
            sys.exit(65)

    def runPrompt(self):
        while True:
            line = input("<lox>>> ")
            if line == "exit()":  # TODO: proper EOF detection
                break
            self.run(line)
            self.hadError = False

    def run(self, source: str):
        scanner = Scanner(self, source)
        tokens = scanner.scanTokens()
        for token in tokens:
            print(token.type)

    def error(self, line: int, message: str):
        self.__report(line, "", message)

    def __report(self, line: int, where: int, message: str):
        print(f"[line {line}] Error{where}: {message}")
        self.hadError = True


if __name__ == "__main__":
    lox = Lox()
    lox.main()
