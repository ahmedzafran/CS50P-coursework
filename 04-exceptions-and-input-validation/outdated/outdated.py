"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
 otherwise known as middle-endian order, which is arguably bad design.
 Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
 Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
   Dates in that format are also ambiguous. Harvard was founded on September 8,
   1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard
 that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order,
   no matter the country, formatting years with four digits, months with two digits,
     and days with two digits, “padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date,
 anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
   wherein the month in the latter might be any of the values in the list below:

[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. If the user’s
input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate
whether a month has 28, 29, 30, or 31 days.

Hints
Recall that a str comes with quite a few methods,
per docs.python.org/3/library/stdtypes.html#string-methods, including split.
Recall that a list comes with quite a few methods,
per docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is index.
Note that you can format an int with leading zeroes with code like
print(f"{n:02}")
wherein, if n is a single digit, it will be prefixed with
 one 0, per docs.python.org/3/library/string.html#format-string-syntax.
"""

def main():
    months = {

      "January":1,
      "February":2,
      "March":3,
      "April":4,
      "May":5,
      "June":6,
      "July":7,
      "August":8,
      "September":9,
      "October":10,
      "November":11,
      "December":12

    }
    y = []
    try:
        while True:
            x = input("Date: ")
            if x.rfind("/")>1:
                x = x.replace(" ", "")
                y = x.split("/")
                if not y[0].isnumeric():
                    continue
                y[1] = int(y[1])
                y[0] = int(y[0])
                y[2] = int(y[2])
                if y[0]<13 and y[1]<32:
                    print(f"{y[2]}-{y[0]:02}-{y[1]:02}")
                    return False

            elif x.rfind(",")>1:
                y = x.split(" ")
                if not y[0].isalpha():
                    continue
                y[1] = y[1].replace(",","")
                y[0] = y[0].lower().capitalize()
                for month in months:
                    if y[0] in month:
                        y[0] = months[month]
                        y[1] = int(y[1])
                        break
                if y[1]<32:
                  print(f"{y[2]}-{y[0]:02}-{y[1]:02}")
                  return False
            else:
                continue









    except:
        pass

main()
