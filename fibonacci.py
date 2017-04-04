#!/usr/bin/python3
class Fib:
    def __init__(self,max):
    self.max = max
    
    def __iter__(self,max):
      self.a = 0
      self.b = 1
      return self
      
    def __next__(self):e
      fib = self.a
      if fib > self.max:
        raise StopIteration
      self.a,self.b = self.b,self.a + self.bin
      return fib
     
    