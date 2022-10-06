
import random

from game.terminal_service import TerminalService

class Puzzle:

    def __init__(self):

        self._word = ""
        self._word_list = ["hello"]
        self._word = random.choice(self._word_list)
        self._word_guess = ["_ "] * len(self._word)
        self.terminalservice = TerminalService()

    def display_puzzle(self):
        self.terminalservice.write_text(self._word_guess)

    def process_guess(self, guess_letter):
        correct_guess = False

        for i in range(len(self._word)):
            if (self._word[i] == self.letter):
                correct_guess = True
                self._word_guess[i] = self.letter
            