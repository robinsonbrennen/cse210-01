from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): Creates the jumper, removes a line, checks for remaining parachute.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): Creates the puzzle, manages guesses.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self._is_playing:
            self._do_outputs()
            self._get_inputs()
            self._do_updates()
            # self._is_playing = False

    def _get_inputs(self):
        """ Args:
            self (Director): An instance of Director.
        """
        guess_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._puzzle.process_guess(guess_letter)
        
    def _do_updates(self):
        """ Args:
            self (Director): An instance of Director.
        """
        pass
        
    def _do_outputs(self):
        """ Args:
            self (Director): An instance of Director.
        """
        self._puzzle._select_word()
        self._jumper._draw_jumper()