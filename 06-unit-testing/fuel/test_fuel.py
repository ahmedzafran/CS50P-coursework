"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3,
restructuring your code per the below, wherein:

convert expects a str in X/Y format as input,
 wherein each of X and Y is an integer, and returns that fraction
 as a percentage rounded to the nearest int between 0 and 100, inclusive.
 If X and/or Y is not an integer, or if X is greater than Y, then convert
 should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
def main():
    ...


def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_fuel.py,
implement two or more functions that collectively test your
implementations of convert and gauge thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_fuel.py
"""
import pytest
from fuel import gauge, convert

def test_convert():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("cat/3")
    with pytest.raises(ValueError):
        convert("4/dog")
    with pytest.raises(ValueError):
        convert("5/3")
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("0/10") == 0
    assert convert("10/10") == 100

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(75) == "75%"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
