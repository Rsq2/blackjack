from random import randint

class Card:
    def __init__(self, suit, face, value, rank):
        self.suit = suit
        self.face = face
        self.value = value
        self.rank = rank
        self.std_symbols = {'Spades' : '♠', 'Diamonds' :  '♦', 'Hearts' : '♥', 'Clubs' : '♣'}

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value

    def set_value(self, new_val):
        self.value = new_val

    #This needs to changed to a switch on/off testing whether the standard deck is being used
    def get_display(self):
        return self.face + self.std_symbols[self.suit]


class Deck:
    def __init__(self, suits, faces, values, ranks):
        self.max_cards = len(suits) * len(faces)
        self.suits = suits
        self.faces = faces
        self.values = values
        self.ranks = ranks
        self.current_cards = []
        self.possible_cards = []
        for suit in self.suits:
            for i, face in enumerate(self.faces): #lol.
                rank = self.ranks.index(face)
                value = values[i]
                new_card = Card(suit, face, value, rank)
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

    def get_ranks(self):
        return self.ranks

    def print_deck(self):
        a_new_deck = standard_deck()
        a_new_deck.shuffle_deck()

        current_cards = a_new_deck.get_current_cards()
        for card in current_cards:
            card_info = []
            card_info.append(int(card.get_rank()))
            card_info.append(str(card.get_suit()))
            card_info.append(str(card.get_face()))
            print(card_info)

def standard_deck():
    std_suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    std_faces = ['2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    std_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    std_rank = std_faces
    return Deck(std_suits, std_faces, std_values, std_rank)
