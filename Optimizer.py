class Optimizer:
    fileLines = []
    index = 0

    sourceName = ""

    lineTypes = ["Hermite", "Bezier"]
    tanTypes = ["InTan", "OutTan"]

    def __init__(self,fileName):
        with open(fileName, "r") as f:
            self.fileLines = f.readlines()
        self.sourceName = fileName

    def LinearizeLineType(self,typeName):
        stringList = self.fileLines
        index = self.index
        stringList[index] =  stringList[index].replace(typeName, "Linear")
        
    def LinearizeTan(self):
        del self.fileLines[self.index]
        self.index -= 1

    def LinearizeAnimations(self):
        while self.index < len(self.fileLines):
            line = self.fileLines[self.index]
            
            for lineType in Optimizer.lineTypes:
                if lineType in line:
                    self.LinearizeLineType(lineType)
                    break
            for tanType in Optimizer.tanTypes:
                if tanType in line:
                    self.LinearizeTan()
                    break

            self.index += 1
            if self.index%100 == 0:
                print ( "Line", self.index, "of",len(self.fileLines) )

    def WriteToFile(self,fileName = ""):
        if fileName == "":
            fileName = self.sourceName.replace(".mdl", "-opt.mdl")
        with open(fileName, "w") as f:
            f.writelines(self.fileLines)

import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        if ".mdl" in sys.argv[1]:
            a = Optimizer(sys.argv[1])
            a.LinearizeAnimations()
            a.WriteToFile()
            print ("Done!")
        else:
            print ("\""+sys.argv[1]+"\"","is not a .mdl file.")
            while True:
                pass
            

    
