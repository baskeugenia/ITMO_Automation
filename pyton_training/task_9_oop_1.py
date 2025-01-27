from task_9_checks import Checks


class Input(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Button(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Title(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc


class Link(Checks):

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

def print_info(ch: Checks):
    print(f'''{ch.text}
* {ch.check_text()} *
{ch.loc}
    ''')


search = Input('input#search', 'SEARCH')
print_info(search)

button = Button('input#button', 'BUTTON')
print_info(button)

input = Input('input#input', 'INPUT')
print_info(input)

link = Link('input#link', 'LINK')
print_info(link)
