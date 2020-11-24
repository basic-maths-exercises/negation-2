import numpy as np

def numberBetween( data, a, b ) :
  nnn = 0
  for d in data : 
    if d>a and d<b : nnn = nnn + 1 
  return nnn
  
def negationBetween( data, a, b ) :
  # Your code goes here
  

# These lines of code allow you to check your code is working
data = np.loadtxt("mydata.dat")
print(numberBetween(data,3,7), "should equal", len(data) - negationBetween(data,3,7))
