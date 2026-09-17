"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
 wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
   how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that
   the tank is essentially empty. And if 99% or more remains, output F
   instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead
prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any
exceptions like ValueError or ZeroDivisionError.
"""

def main():

  prompt = input("please enter a fraction format; x/y: ")
  print(convert(prompt))



def convert(fraction):
    z = []
    for char in fraction:
      z.append(char)
    num = []
    den = []
    for y in range(len(z)):
      try:
        while z[y] != "/":
          num.append(z[y])
          y += 1
        else:
          y += 1
          while y < len(z):
            den.append(z[y])
            y += 1
          break
      except IndexError:
        print("please use \"/\"")
        break
    sn1, sn2 = ("".join(num)), ("".join(den))
    if sn1.isdigit() and sn2.isdigit():
      n1, n2 = int(sn1), int(sn2)
      if n2 == 0:
        raise ZeroDivisionError("Denominator cant be 0")
      elif n1 > n2:
        raise ValueError("x is greater than y")
    else:
      raise ValueError("Numerator or denominator is not an integer")
    p = int(round((n1/n2) * 100, 0))
    return p

def gauge(percentage):
  if percentage < 2:
    p = "E"
    return p
  elif percentage > 98:
    p = "F"
    return p
  else:
    p = str(percentage) + "%"
    return p

if __name__ == "__main__":
  main()
