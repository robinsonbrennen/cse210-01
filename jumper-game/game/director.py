from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:

    def __init__(self):

        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def _display(self):
        self._puzzle.display_puzzle()
        self._jumper.display_jumper()

    def _get_inputs(self):
        self.letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
                    
    def _do_updates(self):
        self.correct_guess = self._puzzle.process_guess(self.letter)

        if self.correct_guess == False:
            self._jumper._remove_line()

            if self._jumper.has_parachute() == False:
                self._is_playing = False
                self._jumper.last_life()

        if self._puzzle.can_keep_guessing() == False:
            self._is_playing = False

    def _do_outputs(self):
        if self._puzzle.can_keep_guessing == False:
            print ("Congratulations you guessed the word!")
            self._is_playing = False