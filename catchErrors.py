#!/usr/bin/python3
def main():
    sourceFile = "test_files/list.txt"
    wrongFile = "test_files/badFile.srt"
    FileRead(sourceFile)
    DemarcationLine()
    LineStrip(sourceFile)
    DemarcationLine()
    CheckFileExtension(wrongFile)

def ReadFile(filename):
    files = open(filename)
    lines = files.readlines()
    for index,line in enumerate(lines):
        print(index, "=", line)

def StripFile(filename):
    files = open(filename)
    for lines in files:
        print (lines.strip())

def RaisingError(filename):
    if filename.endswith(".txt"):
        lines = filename.open();
        for line in lines:
            print(line.strip())
    else:
        raise ValueError("File must end with .txt")

def FileRead(sourceFile):
    try:
        ReadFile(sourceFile)
    except IOError as e:
        print ("Could not open file: ",e)

def LineStrip(sourceFile):
    try:
        StripFile(sourceFile)
    except IOError as e:
        print ("Could not open file: ",e)

def CheckFileExtension(wrongFile):
    try:
        RaisingError(wrongFile)
    except IOError as e:
        print ("Could not open file: ",e)
    except ValueError as e:
        print ("Bad Filename",e)

def DemarcationLine():
    print ("*******************")

if __name__ == "__main__":
    main()
