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

        if self.check_outright_win() == True:
            pass

        else:
            starting_players = self.hand.get_players()
            dealer_number = 0

            # [:] is taking the whole array and making a new copy rather than reference
            # so that it can be modified within the 'for' loop.

            for p in starting_players[:]:
                if p.player_type == 'user':
                    p.set_bet(input(
                        "\nCurrent Money: {0}\nHow much would you like to bet?\n > "
                        .format(p.get_current_money())
                        ))

                    self.evaluate_cards(p)

                elif p.player_type == 'dealer':
                    # IMPLICIT ASSUMPTION: dealer is appended last to the player array
                    dealer_number = self.dealer_behavior(p)

            remaining_players = self.hand.get_players()

            for p in remaining_players[:]:
                if p.player_type == 'user':
                    self.calculate_winners(p, dealer_number)

    def calculate_winners(self, player, dealer_number):
        player_number = self.calculate_hand_value(player)

        if dealer_number == None or player_number > dealer_number:
            print("\n{0} WINS!\n+ ${1}\n".format(
                player.get_name(),
                player.get_bet(),
                ))

            player.set_current_money(player.get_current_money() + player.get_bet())

        elif player_number < dealer_number:
            print("{0} LOSES ... {1}\n".format(
                player.get_name(),
                player_number
                ))

    def calculate_hand_value(self, player):
        current_val = 0
        for card in player.player_hand.current_cards:
            current_val += card.get_value()
        return current_val

    def get_highest_handval(self):
        highest = 0
        for p in self.hand.get_players():
            this_handval = self.calculate_hand_value(p)
            if this_handval > highest:
                highest = this_handval

        return highest

    def evaluate_cards(self, player):
        player.player_hand.times_evaluated += 1

        the_number = self.calculate_hand_value(player)

        if the_number > 21:
            self.bust(player)

        elif the_number < 21:
            self.get_choices(player)

        elif the_number == 21:
            print("Current Hand {0}, Total: {1}\n"
            .format(
                player.player_hand.display_current_hand(),
                self.calculate_hand_value(player)
            ))

            print("\n\t21!\n")
            return the_number

        else:
            print("SOMETHING IS TERRIBLY WRONG HERE.")

    def check_outright_win(self):
        for p in self.hand.get_players():
            if p.player_type == 'dealer':
                dealer_cards = p.player_hand
                dealer_number = self.calculate_hand_value(p)

                if dealer_cards[0].get_face() == 'A' and dealer_cards[1].get_face() in ['10','J', 'Q', 'K']:
                    print ("\nDEALER WINS OUTRIGHT...\n\t{0}".format(
                        dealer_cards.display_current_hand()
                        ))
                    return True

    def dealer_behavior(self, dealer):
        dealer_number = self.calculate_hand_value(dealer)

        if self.hand.players == [dealer]:
            return dealer_number

        if dealer_number == 21:
            print ("\n\t DEALER HITS 21...\n")
            return dealer_number

        elif dealer_number > 21:
            self.bust(dealer)
            return 0

        elif dealer_number in range(17,21):
            self.stay(dealer)
            return dealer_number

        else:
            self.hit(dealer)
            self.dealer_behavior(dealer)

    def stay(self, player):
        final_number = self.calculate_hand_value(player)
        print ("\n\t{0} STAYS at {1}!\n".format(
            player.get_name(),
            final_number
            ))
        return final_number

    def hit(self, player):
        the_card = self.deck.draw_card()
        print("\n\t{0} HITS! ... {1} !\n".format(
            player.get_name(),
            the_card.get_display()
            ))

        player.player_hand.current_cards.append(the_card)

    def split_hand(self, player):
        print("\n\t{0} SPLITS THEIR CARDS!\n".format(player.get_name()))
        split_hand = player.player_hand.get_current_cards()
        second_hand = Player(str(player.get_name() + '- Split Hand'), player.get_bet())

        player.player_hand.set_current_cards(split_hand.pop(0))
        player.player_hand.current_cards.append(self.deck.draw_card())

        second_hand.player_hand.set_current_cards(split_hand.pop())
        second_hand.player_hand.current_cards.append(self.deck.draw_card())
        return self.evaluate_cards(player)

    def double_down(self, player):
        player_bet = player.get_bet()
        new_bet = player_bet * 2

        print("\n{0} DOUBLES DOWN! ... Bet doubled to {1}\n".format(
            player.get_name(),
            player_bet
            ))

        player.set_bet(player_bet)
        player.player_hand.current_cards.append(self.deck.draw_card())

        if self.calculate_hand_value(player) > 21:
            self.bust(player)

        else:
            print("Current Hand {0}, Total: {1}".format(
                player.player_hand.display_current_hand(),
                self.calculate_hand_value(player),
                ))
            self.stay(player)

    def bust(self, player):
        print("\n\t{0} BUSTS! ... {1}\n".format(
            player.get_name(),
            self.calculate_hand_value(player)
            ))
        current_players = self.hand.get_players()
        current_players.remove(player)
        self.hand.set_players(current_players)
        return 0


    def get_choices(self, player):
        cards = player.player_hand.get_current_cards()
        count = player.player_hand.times_evaluated
        choices = ['(S)tay.','(H)it!']
        valid_input = ["s", "h"]

        if cards[0].get_face() == cards[1].get_face():
            choices.append('(Spl)it')
            valid_input.append('spl')

        elif int((cards[0].get_value() + cards[1].get_value())) in range(9,12) and count <= 1:
            if player.get_current_money() > (player.get_bet() * 2):
                choices.append('(D)ouble Down')
                valid_input.append('d')

        return self.set_choice(player, choices, valid_input)

    def set_choice(self, player, choices, valid_input):
        player_choice = str(input("Dealer Hand:\n\nCurrent Hand {0}, Total: {1},  What will you do? \n {2} \n > "
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
                    self.stay(player)

                elif player_choice == "h" and player_choice in valid_input:
                    choice_made = True
                    self.hit(player)
                    self.evaluate_cards(player)

                elif player_choice == "spl" and player_choice in valid_input:
                    choice_made = True
                    self.split_hand(player)

                elif player_choice == "d" and player_choice in valid_input:
                    choice_made = True
                    self.double_down(player)

                else:
                    print("I Don't Recognize That Input...")
                    return self.set_choice(player, choices, valid_input)

            except ValueError:
                print("I Don't Recognize That Input...")
                return self.set_choice(player, choices, valid_input)


this_player = Player('Johnny Test', 150)
#this_other_player = Player('Jane Trial', 150)
this_dealer = Dealer('Dealer', 99999)
test_players = [this_player, this_dealer]
test_deck = cards.standard_deck()
test_deck.shuffle_deck()

this_game = Blackjack(test_players)

this_game.new_hand()
