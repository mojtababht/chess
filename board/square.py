from . import letter_alt


class Square:

    def __init__(self, letter, number, piece=None):
        letter = letter
        number = number
        cord = self.get_cord()
        color = self.get_color()
        piece = piece


    def get_cord(self):
        x = letter_alt[self.letter]
        y = self.number - 1
        return (x, y)

    def get_color(self):
        odd = self.cord.count() % 2
        if odd:
            return 'white'
        return 'black'
