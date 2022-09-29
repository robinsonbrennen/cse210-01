
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
    def _draw_jumper(self):
        for line in self._jumper:
            self.terminalservice.write_text(line)

#be able to remove a piece of itself when incorrect guess occurs = single line
    def _remove_line(self):
        self._jumper.pop(0)
