from random import randint

class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value
        self.std_symbols = {'Spades' : '♠', 'Diamonds' :  '♦', 'Hearts' : '♥', 'Clubs' : '♣'}

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face

    def get_value(self):
        return self.value

    def set_value(self, new_val):
        self.value = new_val

    #This needs to changed to a switch on/off testing whether the standard deck is being used
    def get_display(self):
        return self.face + self.std_symbols[self.suit]


class Deck:
    def __init__(self, suits, faces, values):
        self.max_cards = len(suits) * len(faces)
        self.suits = suits
        self.faces = faces
        self.values = values
        self.current_cards = []
        self.possible_cards = []

        for suit in self.suits:
            for i, face in enumerate(self.faces): #lol.
                value = self.values[face]
                new_card = Card(suit, face, value)
                self.possible_cards.append(new_card)

    def shuffle_deck(self):
        self.current_cards = self.possible_cards

    def draw_card(self):
        return self.current_cards.pop(randint(0, len(self.current_cards) - 1))

    def get_current_cards(self):
        return self.current_cards

    def get_suits(self):
        return self.suits

    def get_values(self):
        return self.get_values

    def get_max_cards(self):
        return self.total_cards

def standard_deck():
    std_suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    std_faces = ['2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    std_values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
    return Deck(std_suits, std_faces, std_values)
