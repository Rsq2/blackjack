import cards

class Player:
    def __init__(self, name, money):
        self.player_type = 'user'
        self.name = name
        self.current_money = money
        self.player_hand = Player_Hand(self)
        self.current_bet = 0

    def get_current_money(self):
        return self.current_money

    def set_current_money(self, new_money):
        self.current_money = new_money

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_hand

    def get_bet(self):
        return self.current_bet

    def set_bet(self, new_bet):

        if new_bet > self.current_money:
            new_bet = int(input("\nInvalid. Enter bet up to ${0}".format(
                self.current_money
                )))

            choice_made = False
            while choice_made == False:
                try:
                    if new_bet <= self.current_money:
                        choice_made = True
                        self.current_money -= new_bet
                        self.bet = new_bet
                    else:
                        new_bet = int(input("\nInvalid input. Enter bet up to ${0}"
                            .format(self.current_money)))

                except ValueError:
                    new_bet = int(input("\nInvalid input. Enter bet up to ${0}".format(
                        self.current_money
                        )))

            else:
                self.current_money -= new_bet
                self.current_bet = new_bet

    def reset_hand(self):
        self.player_hand = Player_Hand(self)

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

class Player_Hand:
    def __init__(self, player):
        self.player = player
        self.current_cards = []
        self.times_evaluated = 0

    def __getitem__(self, i):
        return self.current_cards[i]

    def __repr__(self):
        return list(map(lambda x: x.get_display(), self.current_cards))

    def get_current_cards(self):
        return self.current_cards

    def set_current_cards(self, new_cards):
        self.current_cards = new_cards

    def display_current_hand(self):
        return list(map(lambda x: x.get_display(), self.current_cards))

class Dealer( Player ):
    def __init__(self, name, money):
        Player.__init__(self, name, money)
        self.name = 'Dealer'
        self.player_type = 'dealer'
        self.money = 999999


#new_player = Player(100)
#new_player.test_player()
