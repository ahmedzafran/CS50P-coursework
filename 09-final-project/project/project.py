from art import *
from fpdf import FPDF
import requests

# instantiates the class and class attributes for all the required features of the program
class Shirt_custom(FPDF):
    def __init__(self, text):
        super().__init__()
        self._text = text
        self._price = 15 + (len(text)*5)
        self._user_color = None
        self._color = {
            "1": (0, 0, 0),  # black
            "2": (0, 255, 0),  # green
            "3": (0, 0, 255),  # blue
            "4": (255, 0, 0),  # red
            "5": (255, 255, 255)  # white
        }
        self._color_price = {
            "1": 0,
            "2": 15,
            "3": 15,
            "4": 15,
            "5": 5
        }

# retrieves the shirt from the donwload link
    def get_shirt(self):
        shirt = "https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png"
        response = requests.get(shirt)
        if response.status_code == 200:
            with open("shirtificate.png", "wb") as file:
                file.write(response.content)
            return "shirtificate.png"
        else:
            raise Exception("shirt didn't download")

# creates and positions the users print on the shirt
    def custom_string(self):
        self.set_font("Courier", size=25)
        self.set_y(self.h - (0.75 * self.h))
        lines = text2art(self._text, space=2)
        for line in lines.split("\n"):
            self.cell(0, 10, line, ln=True, align="C")

# set the color of the thread used for stitching the custom print, according to the user's choice
# & calculate the total price of the shirt tinkered by the color chosen
    def coloring(self, user_color):
        if user_color in self._color:
            r, g, b = self._color[user_color]
            self.set_text_color(r, g, b)
            self._price += self._color_price[user_color]
            self._user_color = user_color
        else:
            raise ValueError("Color doesn't exist!!")

# creates the template of the shirt onto the fpdf2 format
    def header(self):
        if self.page_no() == 1:
            x, y = self.w - (0.9 * self.w), self.h - (0.9 * self.h)
            self.image("shirtificate.png", x, y, 170)
            self.set_font("Courier", size=40)
            self.cell(80)
            self.ln(20)

# a tracker for the dynamic value of price
    @property
    def price(self):
        return self._price

# prints a receipt of user details
    def print_receipt(self):
        match self._user_color:
            case "1":
                choice = "black"
            case "2":
                choice = "green"
            case "3":
                choice = "blue"
            case "4":
                choice = "red"
            case "5":
                choice = "white"
        self.add_page()
        self.set_font("Courier", size=20)
        self.set_text_color(0, 0, 0)
        self.ln(10)
        self.cell(0, 10, "Order Receipt", ln=True, align="L")
        self.set_font("Courier", size=10)
        self.ln(10)
        self.cell(0, 10, "="*92, ln=True, align="L")
        self.ln(20)
        self.cell(0, 10, f"Custom print: {self._text}", ln=True, align="L")
        self.cell(0, 10, f"Color: {choice}", ln=True, align="L")
        self.cell(0, 10, f"Total Price: ${self._price}", ln=True, align="L")
        self.ln(140)
        self.cell(0, 10, "="*92, ln=True, align="L")

# the user promoting station
def get_text():
    # can only be 2 characters long input
    print("Welcome, you are allowed to print up to any 2 characters for your custom shirt")
    print("The base shirt will cost 15$ and every character costs 5$ each")
    custom_print = input("Custom Print: ")
    print("You may also choose a custom color for your stitching from the following options:\n" +
          "1. Black + 0$\n" +
          "2. Green + 15$\n" +
          "3. Blue + 15$\n" +
          "4. Red + 15$\n" +
          "5. White + 5$\n")
    custom_color = input("Please enter the number:\n")
    while True:
        if len(custom_print) <= 2:
            return Shirt_custom(custom_print), len(custom_print), custom_color
        else:
            print("That was more than 2 characters!")
            custom_print = input("Custom Print: ")

# program pipeline
def main():
    Shirt, n, color = get_text()
    Shirt.coloring(color)
    Shirt.get_shirt()
    Shirt.add_page()
    Shirt.custom_string()
    Shirt.print_receipt()
    Shirt.output("custom_order.pdf")

if __name__ == "__main__":
    main()
