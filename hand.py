import cards
from player import Player

class Hand:
    """Takes 4 Variables: incoming Deck object, max number of cards, bet for this hand, and an array of leftover cards"""
    def __init__(self, players, deck, hand_size, bet):
        self.deck = deck
        self.bet = bet
        self.players = players
        self.hand_size = hand_size

    def deal(self):
        self.deck.shuffle_deck
        for player in self.players:
            player.set_current_cards([])
            for i in range(self.hand_size):
                player.current_cards.append(self.deck.draw_card())

    def fold(self, this_player):
        self.players -= this_player

    def get_bet(self):
        return self.bet

    def set_bet(self, new_bet):
        self.bet = new_bet

    def get_players(self):
        return self.players

    def set_players(self, new_players):
        self.players = new_players

    def test_hand(self):
        print(a_test_hand.get_bet())
        a_test_hand.set_bet(69342)
        print(a_test_hand.get_bet())

        print(a_test_hand.get_players())
        a_test_hand.set_players([Player(150), Player(2)])
        print('testing "Deal" function')
        a_test_hand.deal()

        for player in self.get_players():
            print(player.display_current_hand())

this_player = Player(150)
test_deck = cards.standard_deck()
test_deck.shuffle_deck()
this_bet = 50

a_test_hand = Hand(this_player, test_deck, 7, this_bet)
a_test_hand.test_hand()
