import pytest
from project import Shirt_custom
import os

# test the price of the shirt with different amount of input characters
def test_character_price():
    shirt = Shirt_custom("J")
    assert shirt._price == 20

    shirt2 = Shirt_custom("Hi")
    assert shirt2._price == 25

# test the api get request for the shirt image
def test_shirt_download():
    shirt = Shirt_custom("J")
    filename = shirt.get_shirt()
    assert os.path.exists(filename)
    os.remove(filename)

# test color pricing
@pytest.mark.parametrize("color_choice,correct_price", [
    ("1", 20), # Black +0
    ("2", 35), # Green +15
    ("3", 35), # Blue +15
    ("4", 35), # Red +15
    ("5", 25) # White +5
])
def test_color_pricing(color_choice, correct_price):
    shirt = Shirt_custom("J") #(price == 20)
    shirt.coloring(color_choice)
    assert shirt._user_color == color_choice
    assert shirt._price == correct_price

if __name__ == "__main__":
    pytest.main()
