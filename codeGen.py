class CodeGen:

    def __init__(self, tab="    "):
        self.code = []
        self.tab = tab
        self.level = 0

    #Adds new lines to code list
    def write(self, lines, indent = 0):
        if isinstance(lines, list):
            for line in lines:
                self.code.append(self.tab * self.level + line)
        else:
            self.code.append(self.tab * self.level + lines)
        self.indent(indent)

    #Indents code by given amount
    def indent(self, indent = 1):
        if self.level + indent >= 0:
            self.level += indent
        else:
            print("Indentation error")

    #Saves code to given filelocation
    def save(self, filename):
        with open(filename, "w") as outfile:
            outfile.write("\n".join(self.code))