import cards
from hand import Hand
from player import Player

class Blackjack( Game ):
    def __init__(self, starting_money, players):
        self.deck = cards.Deck.standard_deck
        self.players = players

    def new_hand(self):
        this_bet = int(input("How much would you like to bet?"))
        this_hand = Hand(self.players, self.deck, this_bet)
        this_hand.deal(2)
        for player in this_hand.get_players():
            evaluate_cards(player)

    def calculate_hand_value(self, current_player):
        for card in current_player.current_cards:
            value += card.get_value()
        return value

    def evaluate_cards(self, player):
        the_number = calculate_hand_value(player)

        if player.player_type == 'user':
            if the_number > 21:
                bust(player)

            elif the_number < 21:
                self.get_choice(player)

            elif the_number == 21:
                print("\n\t21! YOU WIN !!!! \n")
                return True

            else:
                print("SOMETHING IS TERRIBLY WRONG HERE.")

        elif player.player_type == 'dealer':
            the_number = dealer_rules(player, the_number, dealer_cards)
            return the_number

    def dealer_rules(self, dealer, handval):
        dealer_number = handval
        dealer_cards = dealer.get_current_cards()
        if dealer_cards[0].get_value() == 'A' and dealer_cards[1].get_value() in ['10','J', 'Q', 'K']:
            print ("\n\t DEALER WINS OUTRIGHT...\n")
            return True

        while the_number < 17:
            self.hit(dealer)
            the_number = calculate_hand_value(dealer)
            if dealer_number == 21:
                print ("\n\t DEALER HITS 21...\n")
                return True
            elif dealer_number >= 17 and dealer_number < 21:
                return dealer_number

    def stay(self, player):
        print ("\n\t{0} Stays!\n".format(player.get_name()))
        return self.calculate_hand_value(player)

    def hit(self, player):
        player.current_cards.append(self.deck.draw_card())

    def split_hand(self, player):
        current_hand = player.get_current_cads()
        second_hand = Player(str(player.get_name() + '- Split Hand'), player.get_bet())

        player.set_current_cards[current_hand[0]]
        self.hit(player)

        second_hand.set_current_cards[current_hand[1]]
        self.hit(second_hand)

    def double_down(self, player):
        pass

    def bust(self, player):
        pass

    def get_choice(self, player):
        cards = player.get_current_cards
        choices = ['(S)tay.','(H)it!']

        if cards[0] == cards[1]:
            choices.append('(Spl)it')

        elif int((cards[0].get_value + cards[1].get_value)) in range(9,11):
            choices.append('(D)ouble Down')

        player_choice = str(input("Current Hand [{0}] [{1}], Total: {2},  What will you do? \n {3} \n > "
            .format(
                card[0].get_display,
                card[1].get_display,
                card[0].get_value + card[1].get_value,
                choices
            )
        )).lower()

        try:
            if player_choice == "s":
                self.stay(player)
            elif player_choice == "h":
                self.hit(player)
            elif player_choice == "spl":
                self.split_hand(player)
            elif player_choice == "d":
                self.double_down(player)
        except ValueError:
            print("I Don't Recognize That Input...")
            self.get_choice()
