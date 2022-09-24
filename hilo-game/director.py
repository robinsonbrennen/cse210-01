from card import Card


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card ([Card]): An instance of Card
        card2 ([Card]): Another instance of Card
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for one round of play.
        player_guess (string): 
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.card = 0
        self.card2 = 0
        self.is_playing = True
        self.total_score = 300
        self.player_guess = " "
        self.card = Card()
        self.card2 = Card()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        if (self.card.value == 0):
            self.card.draw()

            print(f"The card is: {self.card.value}")
            self.player_guess = input("Higher or lower? [h/l] ")
            self.card2.draw()
            print(f"The card is: {self.card2.value}")

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if (self.player_guess.lower() == "h"):
            if (self.card.value < self.card2.value):
                self.total_score += 100
            else:
                self.total_score -= 75
        elif (self.player_guess.lower() == "l"):
            if (self.card.value > self.card2.value):
                self.total_score += 100
            else:
                self.total_score -= 75

        self.card.value = self.card2.value

        if self.total_score <= 0:
            self.is_playing = False
            print("Game Over")

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.total_score}")
        play_again = input("Play again? [y/n]")
        print("\n")
        if play_again == "n":
            self.is_playing = False
