class Button:

    type: str = 'Button'

    def __init__(self, text, link):
        self.text = text
        self.link = link


home = Button('HOME', '/home')
catalog_msk = Button('CATALOG', '/msk/catalog')

print('button ' + home.text + ' has link ' + home.link)

print('\n')

print('button ' + catalog_msk.text + ' has link ' + catalog_msk.link)


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Clicked locator - {}".format(self.loc)


home_two = ButtonTwo('HOME', '/home', 'button#home')
print(home_two.click())