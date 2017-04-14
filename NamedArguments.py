#!/usr/bin/python3
#NAMED ARGUMENTS
def main():
    NamedArguments(name = "John", surname = "Lock", job = "Fisherman")

def NamedArguments(**args):
    for key in args:
        print (key," = ",args[key])

if __name__ == "__main__":
    main()
