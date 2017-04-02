#!/usr/bin/python3
import re

def main():
    content = open("milan.txt")
    #ReplaceWord(content)
    MatchAndReplace(content)
    
def openFile(filename):
    try:
        content = open(filename)
        return [1,content]
    except FileNotFoundError as e:
        return [0,e]

def ReplaceWord(content):
    content.seek(0)
    for line in content.readlines():
        print(re.sub('Romano','---GATTO---',line),end='')

def MatchAndReplace(content):
    content.seek(0)
    for line in content.readlines():
        match = re.search('Romano',line)
        if match:
            print(line.replace(match.group(),'POOOOOOOLLOOOO'),end='')
if __name__ == "__main__":
    main()
