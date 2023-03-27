from utils.character_set import character_representation
from utils.number_set import get_number_base


class NumberRep:
    def __init__(self, char_number, count = 0):
        self.char = char_number
        self.count = count

    def __str__(self):
        return character_representation(int(self.char))

    def value(self):
        return ((63 * self.count) + self.char) if self.count > 0 else int(self.char)
