
class Rectangle():

    def __init__(self, w:float, h:float):
        self.width = w
        self.height = h

    def perimeter(self) -> float:
        return self.width * 2 + self.height * 2

    def square(self) -> float:
        return self.width * self.height


r1 = Rectangle(1, 1)
print(f'perimeter = {r1.perimeter()}, square = {r1.square()}')
r2 = Rectangle(1.1, 1.1)
print(f'perimeter = {r2.perimeter()}, square = {r2.square()}')
r3 = Rectangle(2, 100)
print(f'perimeter = {r3.perimeter()}, square = {r3.square()}')


class Math:

    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def addition(self) -> float:
        return self.a + self.b

    def subtraction(self) -> float:
        return self.a - self.b

    def multiplication(self) -> float:
        return self.a * self.b

    def division(self) -> float:
        return self.a / self.b

    def print_info(self):
        print(f'''
        {self.a} + {self.b} = {self.addition()}
        {self.a} - {self.b} = {self.subtraction()}
        {self.a} * {self.b} = {self.multiplication()}
        {self.a} / {self.b} = {self.division()}
        ''')


m1 = Math(2, 2)
m1.print_info()

m2 = Math(-1, 2)
m2.print_info()

m3 = Math(7, 5)
m3.print_info()


class Button:

    def __init__(self, text):
        self.type = 'Button'
        self.text = text
        self.loc = ''

    def click(self) -> str:
        return f'Clicked the button {self.text}'


def print_button_and_click(b: Button):
    print(f'{b.text}\n{b.click()}\n')


b1 = Button('Text Box')
print_button_and_click(b1)
b2 = Button('Check Box')
print_button_and_click(b2)
b3 = Button('Radion Button')
print_button_and_click(b3)
b4 = Button('Web Tables')
print_button_and_click(b4)
b5 = Button('Buttons')
print_button_and_click(b5)
b6 = Button('Links')
print_button_and_click(b6)
b7 = Button('Broken Links - Images')
print_button_and_click(b7)
b8 = Button('Upload and Download')
print_button_and_click(b8)
b9 = Button('Dynamic Properties')
print_button_and_click(b9)
