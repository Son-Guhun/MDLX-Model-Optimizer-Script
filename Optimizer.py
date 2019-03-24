import sys
import subprocess
import os
import time

from py2exeUtils import DIRECTORY
from py2exeUtils import path

class Model:
    mdlx_path = DIRECTORY+"mdlxconv\\converter.exe" \
                if os.path.exists(DIRECTORY+'mdlxconv') \
                else path.up(DIRECTORY)+'mdlxconv\\converter.exe'


    lineTypes = ["Hermite", "Bezier"]
    tanTypes = ["InTan", "OutTan"]

    def __init__(self,file_name):
        if ".mdx" == file_name[-4:]:
            subprocess.call([Model.mdlx_path, file_name])
            file_name = file_name[:-4] + '.mdl'
            self.is_mdx = True
        elif ".mdl" == file_name[-4:]:
            self.is_mdx = False
        else:
            raise ValueError('File is not an mdx or mdl file')
            
        with open(file_name, "r") as f:
            self._file_lines = f.readlines()
        self.sourceName = file_name
        self._index = 0
        
        if self.is_mdx:
            os.remove(file_name)

    def _linearize_line_type(self,typeName):
        stringList = self._file_lines
        index = self._index
        stringList[index] =  stringList[index].replace(typeName, "Linear")
        
    def _linearize_tan(self):
        del self._file_lines[self._index]
        self._index -= 1

    def linearize_animations(self):
        while self._index < len(self._file_lines):
            line = self._file_lines[self._index]
            
            for lineType in Model.lineTypes:
                if lineType in line:
                    self._linearize_line_type(lineType)
                    break
            for tanType in Model.tanTypes:
                if tanType in line:
                    self._linearize_tan()
                    break

            self._index += 1
            if self._index%100 == 0:
                print ( "Line", self._index, "of",len(self._file_lines) )

    def write_to_file(self,file_name = ""):
        if file_name == "":
            file_name = self.sourceName.replace(".mdl", "-opt.mdl")
        with open(file_name, "w") as f:
            f.writelines(self._file_lines)
        if self.is_mdx:
            subprocess.call([Model.mdlx_path, file_name])
            os.remove(file_name)
        return file_name

print DIRECTORY

try:
    if __name__ == "__main__":
        if len(sys.argv) >= 2:
            for file_name in sys.argv[1:]:
                print file_name
                try:
                    a = Model(file_name)
                except ValueError as error:
                    print error.message
                    while True:
                        time.sleep(1)
                a.linearize_animations()
                file_name = a.write_to_file()
                print ("Done!")
        else:
            while True:
                time.sleep(1)
                print sys.argv
except Exception as error:
    while True:
        time.sleep(1)
        print error
        print sys.argv