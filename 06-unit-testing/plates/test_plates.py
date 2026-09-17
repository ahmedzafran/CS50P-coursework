"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2,
 restructuring your code per the below,
 wherein is_valid still expects a str as input and returns
   True if that str meets all requirements and False if it does not,
   but main is only called if the value of __name__ is "__main__":

def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_plates.py,
implement four or more functions that collectively test your implementation of is_valid thoroughly,
 each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py
"""
from plates import is_valid

def test_2char():
    assert is_valid("AA") == True

def test_3char():
    assert is_valid("AA1") == True


def test_4char():
    assert is_valid("AA11") == True

def test_5char():
    assert is_valid("AAB11") == True

def test_6char():
    assert is_valid("AAV112") == True

def test_1st_al():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAA1112") == False

def test_num_place():
    assert is_valid("AA1A") == False

def test_zero():
    assert is_valid("AA0") == False

def test_isalphanum():
    assert is_valid("AA!1") == False

