import cards
from hand import Hand
from player import Player

class Blackjack( Game ):
    def __init__(self, deck, starting_money, players):
        self.deck = cards.Deck.standard_deck
        self.players = players

    def new_hand(self):
        this_hand = Hand.deal()

    def calculate_hand_value(self, current_player):
        for card in current_player.current_cards:
            value += card.get_value()
        return value

    def evaluate_cards(self, player):
        for player in self.players:
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
                dealer_cards = player.get_current_cards
                if dealer_cards[0].get_value() == 'A' and dealer_cards[1].get_value() in ['10','J', 'Q', 'K']:
                    print ("\n\t DEALER WINS...\n")
                    return True
                while the_number < 17:
                    hit(player)



    def stay(self, player):
        print ("\n\tSTAY!\n")
        self.calculate_hand_value(player)

    def hit(self, player):
        pass

    def split(self, player):
        pass

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
                self.stay()
            elif player_choice == "h":
                self.hit()
            elif player_choice == "spl":
                self.split_hand()
            elif player_choice == "d":
                self.double_down()
        except ValueError:
            print("I Don't Recognize That Input...")
            self.get_choice()
