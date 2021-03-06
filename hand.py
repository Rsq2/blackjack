import cards
from player import Player

class Hand:
    def __init__(self, players, deck):
        self.deck = deck
        self.players = players
        self.winners = []

    def deal(self, hand_size):
        self.deck.shuffle_deck
        for player in self.players:
            player.player_hand.set_current_cards([])
            for i in range(hand_size):
                player.player_hand.current_cards.append(self.deck.draw_card())

    def fold(self, this_player):
        self.players -= this_player

    def get_players(self):
        return self.players

    def set_players(self, new_players):
        self.players = new_players

    def get_dealer(self):
        return self.get_dealer

    def set_dealer(self, new_dealer):
        self.dealer = new_dealer

    def get_winners(self, winners):
        return self.winners

    def set_winners(self, winners):
        self.winners = winners

    def get_playernames(self):
        return [i.get_name() for i in self.players]

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

#this_player = Player(150)
#test_deck = cards.standard_deck()
#test_deck.shuffle_deck()
#this_bet = 50

#a_test_hand = Hand(this_player, test_deck, 7, this_bet)
#a_test_hand.test_hand()
