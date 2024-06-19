from . import letter_alt


class Square:

    def __init__(self, letter, number, piece=None):
        self.letter = letter
        self.number = number
        self.cord = self.get_cord()
        self.color = self.get_color()
        self.piece = piece


    def get_cord(self):
        x = letter_alt[self.letter]
        y = self.number - 1
        return (x, y)

    def get_color(self):
        odd = (self.cord[0] + self.cord[1]) % 2
        if odd:
            return 'white'
        return 'black'
