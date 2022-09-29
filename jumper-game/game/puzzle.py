
import random

from game.terminal_service import TerminalService

class Puzzle:

    def __init__(self):

        self.terminalservice = TerminalService()
        self._word_list = ["hello", "puzzle", "hyperactive", "pnumonics", "bluff"]
        self._word_selected = random.choice(self._word_list)

        self._word_guess = ["_ "] * len(self._word_selected)


    def _select_word(self):
        self.terminalservice.write_text(self._word_guess)


    def process_guess(self, guess_letter):

        for i in range(len(self._word_selected)):
            
            if guess_letter == self._word_selected[i]:
                
                self._word_guess[i] = guess_letter
