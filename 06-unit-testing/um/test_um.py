from um import count as c
import pytest

def test_count():
    assert c("hi um there um") == 2
    assert c("um so theres um um") == 3

def test_combined():
    assert c("yummy yumm yum um") == 1
    assert c("gummy bears are um good um right") == 2

def test_none():
    assert c("hi there so hi") == 0
    assert c(" yeah theres none here") == 0

def test_case():
    assert c(" hi UM so lets go out") == 1
    assert c("uM lets UM Um yeah") ==  3

