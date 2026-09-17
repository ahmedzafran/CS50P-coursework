from numb3rs import validate as val
import pytest


def test_true():
    assert val("255.255.255.255") is True
    assert val("0.0.0.0") is True
    assert val("12.2.0.255") is True
    assert val("99.99.99.99") is True
    assert val("100.100.100.100") is True



def test_false():
    assert val("275.0.256.255") is False
    assert val("0.0.0") is False
    assert val("-1.-1.-2.-1") is False
    assert val("20.20.20.290") is False
    assert val("0") is False

def test_format():
    assert val("0. 0.0.0") is False
    assert val("dog") is  False
    assert val("123") is False
    assert val("10.10.10.10.10") is False




