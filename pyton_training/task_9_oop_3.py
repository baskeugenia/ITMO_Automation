class Soda:

    def __init__(self, ing:str = ''):
        self.ing = ing

    def show_my_drink(self):
        print(f'Soda with {self.ing}' if self.ing else 'Regular soda')


soda1 = Soda()
soda1.show_my_drink()

soda2 = Soda('strawberry')
soda2.show_my_drink()

