class Scanner:
    def __init__(self, source):
        self.source = source

    def scanTokens(self):
        return self.source.split(' ')
