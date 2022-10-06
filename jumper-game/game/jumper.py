from game.terminal_service import TerminalService
from game.terminal_service import TerminalService


class Jumper:

    def __init__(self):
        
        self.terminalservice = TerminalService()

        self._jumper = [
            "   _____",
            "  /_____\\",
            "  \     /",
            "   \   /",
            "     O",
            "    /|\\",
            "    / \\",
            "",
            "^^^^^^^^^^^",
        ]

#draw itself
    def display_jumper(self):
        for line in self._jumper:
            self.terminalservice.write_text(line)

#be able to remove a piece of itself when incorrect guess occurs = single line
    def _remove_line(self):
        self._jumper.pop(0)

    

    def has_parachute(self):
        if self._jumper == False:
            pass


    # def _place_x(self):
    #     pass