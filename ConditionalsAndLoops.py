#!/usr/bin/python3
def main():
    try:
        places = open('lista.txt')
        if places.read() == 0:
            print ("The file is empty")
        else:
            places.seek(0)
            ##list all the cities
            for place in places.read():
                print (place,end="")    
            places.seek(0)
            ##list all the cities enumerated // use readlines       
            for (index,place) in enumerate(places.readlines()):
                print (index,place,end="")
        places.close()
    except FileNotFoundError:
        print ("File not found")
    
if __name__ == "__main__":
    main()
  
