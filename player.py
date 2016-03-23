import cards

class Player:
    def __init__(self, name, money):
        self.player_type = 'user'
        self.name = name
        self.current_money = money
        self.current_cards = []

    def get_current_money(self):
        return self.current_money

    def set_current_money(self, new_money):
        self.current_money = new_money

    def get_current_cards(self):
        return self.current_cards

    def set_current_cards(self, new_cards):
        self.current_cards = new_cards

    def display_current_hand(self):
        return list(map(lambda x: x.get_display(), self.current_cards))

# This wont be used for blackjack... but is neccesary for many other card games. Need to figure out how to identify each card in the display for selection.
    #def discard(self, num):
        #for i in range(num):
            #choice = str(input("\nCHOOSE CARD TO DISCARD: {0}\n> "
                #.format(self.display_current_hand())
                #))
            #try:
                #if choice in self.current_cards.get_value or choice == self.current_cards.get_
                    #del(self.current_cards[choice])
                #else:
                    #print("I Don't Recognize That Input")
                    #self.discard(num - i)
            #except ValueError:
                #print("I Don't Recognize That Input")
                #self.discard(num - i)

    def test_player(self):
        this_player = Player(150)
        test_deck = cards.standard_deck()
        test_deck.shuffle_deck()
        test_hand = []
        for i in range(3):
            test_hand.append(test_deck.draw_card())

        this_player.set_current_cards(test_hand)

        print(this_player.display_current_hand())
        print(this_player.get_current_money())

class Dealer( Player ):
    def __init__(self, name, cards, money):
        Player.__init__(self, name, cards, money)
        self.name = 'Dealer'
        self.player_type = 'dealer'

    def dealer_stuff_goes_here(or_something):
        pass
#new_player = Player(100)
#new_player.test_player()
