from random import randint

class Card:
    def __init__(self, suit, value, rank):
        self.suit = suit
        self.value = value
        self.rank = rank
        self.std_symbols = {'Spades' : '♠', 'Diamonds' :  '♦', 'Hearts' : '♥', 'Clubs' : '♣'}

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_rank(self):
        return self.rank

    #This needs to changed to a switch on/off testing whether the standard deck is being used
    def get_display(self):
        return self.value + self.std_symbols[self.suit]


class Deck:
    def __init__(self, suits, values, ranks):
        self.max_cards = len(suits) * len(values)
        self.suits = suits
        self.values = values
        self.ranks = ranks
        self.current_cards = []
        self.possible_combinations = []
        for suit in self.suits:
            for value in self.values:
                rank = self.ranks.index(value)
                new_card = Card(suit, value, rank)
                self.possible_combinations.append(new_card)

    def shuffle_deck(self):
        self.current_cards = self.possible_combinations

    def draw_card(self):
        return self.current_cards.pop(randint(0, len(self.current_cards) - 1))

    def get_current_cards(self):
        return self.current_cards

    def get_suits(self):
        return self.suits

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
            card_info.append(str(card.get_value()))
            print(card_info)

def standard_deck():
    std_suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    std_values = ['2', '3','4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    std_rank = std_values
    return Deck(std_suits, std_values, std_rank)
