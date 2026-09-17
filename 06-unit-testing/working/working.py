"""
Whereas most countries use a 24-hour clock,
 the United States tends to use a 12-hour clock. Accordingly,
   instead of “09:00 to 17:00”, many Americans would say they work
   “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”), wherein “AM” is an abbreviation for
   “ante meridiem” and “PM” is an abbreviation for “post meridiem”,
     wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called
convert that expects a str in either of the 12-hour formats
 below and returns the corresponding str in 24-hour format
   (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized
   (with no periods therein) and that there will be a space before each.
   Assume that these times are representative of actual times,
   not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is
not in either of those formats or if either time is invalid
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s
 hours will start ante meridiem and end post meridiem;
   someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome
to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You’re welcome,
but not required, to use re and/or sys.
"""

import re
import sys


def main():
    try:
      print(convert(input("Hours: ")))
    except ValueError as e:
        sys.exit(e)

def convert(s):
    formula = r"""
    ^(1[0-2]|[1-9])(:[0-5][0-9])?
    \s(AM|PM)
    \sto
    \s(1[0-2]|[1-9])(:[0-5][0-9])?
    \s(AM|PM)$
    """
    hours = re.search(formula,s,re.VERBOSE)
    if hours:
      fh, lh = convert24(hours.group(3),hours.group(1)), convert24(hours.group(6),hours.group(4))
      fm, lm = hours.group(2), hours.group(5)
      if fm is None and lm is None:
        fm, lm = 0, 0
        return f"{fh}:{fm:02d} to {lh}:{lm:02d}"
      elif fm != None and lm is None:
        lm = 0
        return f"{fh}{fm} to {lh}:{lm:02d}"
      elif fm is None and lm != None:
         fm = 0
         return f"{fh}:{fm:02d} to {lh}{lm}"
      elif fm != None and lm != None:
         return f"{fh}{fm} to {lh}{lm}"
    else:
      raise ValueError("ValueError")


def convert24(a,b):
  if a == "PM":
      if b != "12":
        b = int(b) + 12
        return f"{int(b):02d}"
      else:
         return f"{int(b):02d}"
  elif a == "AM":
     if b == "12":
        b = 0
        return f"{int(b):02d}"
     else:
        return f"{int(b):02d}"


if __name__ == "__main__":
    main()
