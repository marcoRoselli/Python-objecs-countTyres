#!/usr/bin/python3
###define a class

class Cars:
  def __init__(self,tyres = 4,fuel=100):
    self.tyres = tyres
    self.fuel = fuel
  def countTyres(self):
    return self.tyres

def main():
  tyres = int(input ("Please state the number of tyres "))
  myVehicle = Cars(tyres)

  ###conditionals
  if myVehicle.tyres == 2:
    print ("You have a mopet")
  elif myVehicle.tyres == 4:
    print ("You have a car")
  elif myVehicle.tyres == 6:
    print ("You have a lorry")
  else:
    print ("You have something else that I don't know")

  ##conditional expression or ternary operator
  test = "more than 2 tyres" if myVehicle.tyres >2 else "less than 3 tyres"
  print (test)

  if myVehicle.tyres > 2: print ("again more than 2 tyres")
  else:print ("again less than 3 tyres")

  ##while
  while myVehicle.fuel > 0:
    print ("fuel is ok {}".format(myVehicle.fuel))
    myVehicle.fuel-=30
  print ("Fuel completely depleted, now you walk")  
   
if __name__ == "__main__":
  main()
  
