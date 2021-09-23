import math
import sys
def quadratic(a,b,c):
    x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    string = f"({-b}+-√{b*b-4*a*c})/{2*a}"
    return(x1, x2, string)
if(__name__ == "__main__"):
  print(sys.argv)
  a = float(sys.argv[1])
  b = float(sys.argv[2])
  c = float(sys.argv[3])
  print(quadratic(a,b,c))

