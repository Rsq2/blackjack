import cards
from hand import Hand
from player import Player, Dealer

class Blackjack:
    def __init__(self, players):
        self.deck = cards.standard_deck()
        self.players = players
        self.hand = 0

    def new_hand(self):
        self.hand = Hand(self.players, self.deck)
        self.deck.shuffle_deck()
        self.hand.deal(2)
        for player in self.hand.get_players():
            this_bet = 5 #int(input("How much would you like to bet?"))
            playerwins = False
            player_wins = self.evaluate_cards(player)

    def calculate_hand_value(self, current_player):
        current_val = 0
        for card in current_player.current_cards:
            current_val += card.get_value()
        return current_val

    def evaluate_cards(self, player):
        the_number = self.calculate_hand_value(player)

        if player.player_type == 'user':
            if the_number > 21:
                self.bust(player)

            elif the_number < 21:
                self.get_choice(player)

            elif the_number == 21:
                print("Current Hand [{0}], Total: {2}\n"
            .format(
                player.display_current_hand(),
                self.calculate_hand_value(player)))

                print("\n\t21!\n")
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
        print ("\n\t{0} STAYS!\n".format(player.get_name()))
        return self.calculate_hand_value(player)

    def hit(self, player):
        print("\n{0} HITS!\n".format(player.get_name()))
        player.current_cards.append(self.deck.draw_card())
        self.evaluate_cards(player)

    def split_hand(self, player):
        print("\n{0} SPLITS THEIR CARDS!\n".format(player.get_name()))
        current_hand = player.get_current_cards()
        second_hand = Player(str(player.get_name() + '- Split Hand'), player.get_bet())

        player.set_current_cards[current_hand[0]]
        self.hit(player)

        second_hand.set_current_cards[current_hand[1]]
        self.hit(second_hand)

    def double_down(self, player):
        print("\n{0} DOUBLES DOWN!\n".format(player.get_name()))
        doubled_bet = player.get_bet() * 2
        player.set_bet(doubled_bet)
        self.hit(player)
        self.stay(player)
        return self.evaluate_cards(player)

    def bust(self, player):
        print("\n{0} BUSTS!\n".format(player.get_name()))
        current_players = self.hand.get_players()
        del current_players[player]
        self.hand.set_players(current_players)

    def get_choice(self, player):
        cards = player.get_current_cards()
        choices = ['(S)tay.','(H)it!']
        valid_input = ["s", "h"]

        if cards[0].get_face() == cards[1].get_face():
            choices.append('(Spl)it')
            valid_input.append('spl')

        elif int((cards[0].get_value() + cards[1].get_value())) in range(9,11):
            choices.append('(D)ouble Down')
            valid_input.append('d')

        player_choice = str(input("Current Hand [{0}] [{1}], Total: {2},  What will you do? \n {3} \n > "
            .format(
                cards[0].get_display(),
                cards[1].get_display(),
                self.calculate_hand_value(player),
                choices
            )
        )).lower()

        try:
            if player_choice == "s" and player_choice in valid_input:
                return self.stay(player)
            elif player_choice == "h" and player_choice in valid_input:
                return self.hit(player)
            elif player_choice == "spl" and player_choice in valid_input:
                return self.split_hand(player)
            elif player_choice == "d" and player_choice in valid_input:
                return self.double_down(player)
            else:
                print("I Don't Recognize That Input...")
                self.get_choice()

        except ValueError:
            print("I Don't Recognize That Input...")
            self.get_choice()


this_player = Player('Johnny Test', 150)
this_dealer = Dealer('Dealer', 99999)
test_players = [this_player, this_dealer]
test_deck = cards.standard_deck()
test_deck.shuffle_deck()

this_game = Blackjack(test_players)

this_game.new_hand()


