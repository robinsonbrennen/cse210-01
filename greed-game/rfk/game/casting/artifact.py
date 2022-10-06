from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor! 
class Artifact(Actor):

    def _init_(self):
        super()._init_()
        self._points = 0

    def get_points(self):
        if (self.get_text() == "*"):
            self._points = 1
        else:
            self._points = -1

        return self._points
