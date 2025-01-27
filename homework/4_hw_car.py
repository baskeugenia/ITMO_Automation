
class Car:

    def __init__(self):
        self.color = ''
        self.type = ''
        self.year = ''

    def run(self):
        print('Car is running')

    def stop(self):
        print('Car stopped')

    def set_year(self, y: int):
        self.year = y

    def set_type(self, t: str):
        self.type = t

    def set_color(self, c: str):
        self.color = c


c1 = Car()
c1.set_type('BMW')
c1.set_color('red')
c1.set_year('1999')
c1.run()
c1.stop()

c2 = Car()
c2.set_type('Audi')
c2.set_color('blue-grey metallic')
c2.set_year('2025')
c2.run()
c2.stop()