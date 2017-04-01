#!/usr/bin/python3
###define a class

class Cars:
  def __init__(self,tyres = 4):
    self.tyres = tyres

  def countTyres(self):
    return self.tyres

def main():
  tyres = input ("Please state the number of tyres ")
  Car = Cars(tyres)
  print (Car.countTyres())
if __name__ == "__main__":
  main()
  
