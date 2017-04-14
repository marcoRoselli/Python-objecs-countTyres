#!/usr/bin/python3
#GENERATORS AND YIELD
#1.
def generator_function():
    yield 1
    yield 2
    yield 55

for value in generator_function():
    print (type(value))

#2.comparison yield/no yield
def main():
    print ("This is printed using yield")
    for index in RangeFunction(0,10,1):
        print (index, end=" ")

    print ("\nThis is printed without yield")
    RangeFunctionNoYield(0,10,1)    

def RangeFunction(start,stop,step):
    i = start
    while i <= stop:
        yield i
        i+=step

def RangeFunctionNoYield(start,stop,step):
    for i in range (start,stop):
        print (i,end=" ")
        i += step
            
if __name__ == "__main__":
    main()

    
