from working import convert as cv
import pytest

def test_no_mins():
    assert cv("9 AM to 5 PM") == "09:00 to 17:00"
    assert cv("10 AM to 7 PM") == "10:00 to 19:00"
    assert cv("1 AM to 3 AM") == "01:00 to 03:00"
    assert cv("6 AM to 6 PM") == "06:00 to 18:00"
def test_got_mins():
    assert cv("9:30 AM to 5:00 PM") == "09:30 to 17:00"
    assert cv("10:35 AM to 3:55 PM") == "10:35 to 15:55"
    assert cv("7:00 AM to 6:30 PM") == "07:00 to 18:30"
    assert cv("5:43 AM to 4:48 PM") == "05:43 to 16:48"
def test_post_meridiem():
    assert cv("5 PM to 12 AM") == "17:00 to 00:00"
    assert cv("7:47 PM to 8:33 AM") == "19:47 to 08:33"
    assert cv("9:30 PM to 8:30 PM") == "21:30 to 20:30"
def test_invalid_input():
    with pytest.raises(ValueError):
        cv("9:77 PM to 12:90 AM")
def test_invalid_format():
    with pytest.raises(ValueError):
        cv("9:30 AM 12:00 PM")
