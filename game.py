class Game:
    def __init__(self, graphics, game_type):
        self.hand_size = 0
        self.graphics = graphics

    def add_players(self):
        pass

    def new_game(self):
        for player in self.hand.get_players():
            this_bet = 5 #int(input("How much would you like to bet?"))
            playerwins = False
            player_wins = self.evaluate_cards(player)


#repr method in game class
#printing logic happens here ... check whose playing ... current_player... format a string dynamically
