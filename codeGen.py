

class CodeGen:

    def __init__(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def write(self, lines: list, indent = 0):
        for line in lines:
            self.code.append(self.tab * self.level + line)
        self.indent(indent)

    def write(self, line: str, indent = 0):
        self.code.append(self.tab * self.level + line)
        self.indent(indent)

    def indent(self, indent = 1):
        if self.level + indent >= 0:
            self.level += indent
        else:
            print("Indentation error")

    def save(self, filename):
        with open(filename, "w") as outfile:
            outfile.write("\n".join(self.code))