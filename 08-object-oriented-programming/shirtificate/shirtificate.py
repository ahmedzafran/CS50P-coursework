from fpdf import FPDF


class Shirtificate(FPDF):
    def __init__(self, name):
        super().__init__()
        if isinstance(name, str):
             self._name = name
        else:
            raise ValueError()

    def student_name(self):
        self.set_font("arial", size= 25)
        self.set_text_color(255, 255, 255)
        self.cell(0, (self.h*0.7), f"{self._name} took CS50", align="C")


    def header(self):
        # Rendering logo:
        x, y = self.w - (0.9*self.w), self.h - (0.75*self.h)
        self.image("shirtificate.png", x, y, 170)
        # Setting font: helvetica bold 15
        self.set_font("arial", size= 40)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell((self.w-(0.8*self.w)), (self.h-(0.8*self.h)), "CS50 Shirtificate", align="C")
        # Performing a line break:
        self.ln(20)


def get_name():
    student_name = input("Name: ")
    return Shirtificate(student_name)

def main():
    Student = get_name()
    Student.add_page()
    Student.student_name()
    Student.output("shirtificate.pdf")

if __name__ == "__main__":
    main()

