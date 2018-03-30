import sys
import subprocess

def Main():
    """Converts a MDX file to MDL, optimizes it, then converts it back to MDX."""
    if len(sys.argv) >2:
        fileName = sys.argv[1]
        if ".mdx" in fileName:
            p = subprocess.call(["MdlxConv_1.04.exe", fileName])
            fileName = fileName.replace(".mdx",".mdl")
        subprocess.call(["python","Optimizer.py", fileName])
        fileName = fileName.replace(".mdl","-opt.mdl")
        subprocess.call(["MdlxConv_1.04.exe", fileName])
        
if __name__ == "__main__":
    Main()
