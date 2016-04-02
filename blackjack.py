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
            new_count = 0
            player_handval = self.evaluate_cards(player, new_count)
            print (player_handval)

    def calculate_winners(self):
        pass

    def calculate_hand_value(self, player):
        current_val = 0
        for card in player.player_hand.current_cards:
            current_val += card.get_value()
        return current_val

    def evaluate_cards(self, player, count):
        count += 1
        the_number = self.calculate_hand_value(player)

        if player.player_type == 'user' and the_number != True:
            if the_number > 21:
                self.bust(player)

            elif the_number < 21:
                return self.get_choice(player, count)

            elif the_number == 21:
                print("Current Hand {0}, Total: {1}\n"
                .format(
                    player.player_hand.display_current_hand(),
                    self.calculate_hand_value(player)
                ))

                print("\n\t21!\n")
                return True

            else:
                print("SOMETHING IS TERRIBLY WRONG HERE.")

        elif player.player_type == 'dealer' and the_number != True:
            dealer_number = self.dealer_behavior(player, the_number)
            return dealer_number

        else:
            return player, count

    def dealer_behavior(self, dealer, count):
        dealer_cards = dealer.player_hand
        dealer_number = self.calculate_hand_value(dealer)

        if dealer_cards[0].get_face() == 'A' and dealer_cards[1].get_face() in ['10','J', 'Q', 'K']:
            print ("\n\t DEALER WINS OUTRIGHT...\n{0}".format(dealer_cards.display_current_hand()))
            return True

        while dealer_number < 17:
            self.hit(dealer, count)
            dealer_number = self.calculate_hand_value(dealer)
            if dealer_number == 21:
                print ("\n\t DEALER HITS 21...\n")
                return dealer_number
            elif dealer_number >= 17 and dealer_number < 21:
                return dealer_number

    def stay(self, player):
        print ("\n\t{0} STAYS!\n".format(player.get_name()))
        return self.calculate_hand_value(player)

    def hit(self, player, count):
        print("\n{0} HITS!\n".format(player.get_name()))
        player.player_hand.current_cards.append(self.deck.draw_card())
        return self.evaluate_cards(player, count)

    def split_hand(self, player):
        print("\n{0} SPLITS THEIR CARDS!\n".format(player.get_name()))
        current_hand = player.get_current_cards()
        second_hand = Player(str(player.get_name() + '- Split Hand'), player.get_bet())

        player.set_current_cards[current_hand[0]]
        self.hit(player, count)

        second_hand.set_current_cards[current_hand[1]]
        self.hit(second_hand, count)

    def double_down(self, player, count):
        print("\n{0} DOUBLES DOWN!\n".format(player.get_name()))
        doubled_bet = player.get_bet() * 2
        player.set_bet(doubled_bet)
        self.hit(player, count)
        return self.stay(player)

    def bust(self, player):
        print("\n{0} BUSTS!\n".format(player.get_name()))
        remaining_players = self.hand.get_players()
        del remaining_players[remaining_players.index(player)]
        self.hand.set_players(remaining_players)
        return self.calculate_hand_value(player)

    def get_choice(self, player, count):
        cards = player.player_hand.get_current_cards()
        choices = ['(S)tay.','(H)it!']
        valid_input = ["s", "h"]

        if cards[0].get_face() == cards[1].get_face():
            choices.append('(Spl)it')
            valid_input.append('spl')

        elif int((cards[0].get_value() + cards[1].get_value())) in range(9,11) and count <= 1:
            choices.append('(D)ouble Down')
            valid_input.append('d')

        player_choice = str(input("\nCurrent Hand {0}, Total: {1},  What will you do? \n {2} \n > "
            .format(
                player.player_hand.display_current_hand(),
                self.calculate_hand_value(player),
                choices
            )
        )).lower()

        choice_made = False
        while choice_made == False:
            try:
                if player_choice == "s" and player_choice in valid_input:
                    choice_made = True
                    return self.stay(player)

                elif player_choice == "h" and player_choice in valid_input:
                    choice_made = True
                    return self.hit(player, count)

                elif player_choice == "spl" and player_choice in valid_input:
                    choice_made = True
                    return self.split_hand(player, count)

                elif player_choice == "d" and player_choice in valid_input:
                    choice_made = True
                    return self.double_down(player, count)

                else:
                    print("I Don't Recognize That Input...")


            except ValueError:
                print("I Don't Recognize That Input...")


this_player = Player('Johnny Test', 150)
this_dealer = Dealer('Dealer', 99999)
test_players = [this_player, this_dealer]
test_deck = cards.standard_deck()
test_deck.shuffle_deck()

this_game = Blackjack(test_players)

this_game.new_hand()
