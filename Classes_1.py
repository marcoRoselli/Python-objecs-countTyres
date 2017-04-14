#!/usr/bin/python3
class Robot:
    def _init_(self):
        pass
    def WalkLikeARobot(self):
        print("walks like a robot")
    def CareLikeARobot(self):
        print("takes care like a robot")

robu1 = Robot()
print (type(robu1))
print (id(robu1))

robu2 = Robot()
print (type(robu2))
print (id(robu2))
del robu2

def main():
    robu = Robot()
    print (type(robu))
    print (id(robu))

if __name__ == "__main__":
    main()
    
