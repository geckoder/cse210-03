class Jumper:

    def __init__(self):
        self._jumper_list = ["  ___  ", " /___\ ", " \   / ",
                             "  \ /  ", "   O   ", "  /|\  ", "  / \  "]
        # Sets a list that draws the jumper

    def draw_jumper(self, wrong_guesses):
        # takes an argument for wrong_guesses. This is an int
        self._list = self._jumper_list
        for i in range(wrong_guesses, len(self._list)):
            if wrong_guesses > 3:
                self._list[4] = "   x   "
            print(self._list[i])
            # prints the jumper minus the wrong guesses.
            # if there are enough bad guesses, his head becomes an x
