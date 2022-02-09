from wordHandler import ProcessWord
from jumper import Jumper
from winner import Winner

# Directs the order of the game play. Calls and imports the other classes


class Director:

    def __init__(self):
        self._jumper = Jumper()
        self.winning = Winner()
        self.word = ProcessWord("michelle")
        """
        Maybe we can create a word bank where a 
        word is randomly picked from the list?
        """

    def start_game(self):
        """
        The while loop will need to be ended when the condition 
        for either winning or losing is met, not count :)
        """
        count = 0
        guess = input("Enter a letter: ")
        updatedWord = self.word.generateInitialWordDisplay(guess)
        while count < 10:
            wrong_guesses = 0
            self._print_jumper(wrong_guesses)
            guess2 = input("Enter a letter: ")
            updatedWord = self.word.updateWordDisplay(updatedWord, guess2)
            count += 1

    def _print_jumper(self, wrong_guesses):
        # prints the jumper with the argument for the number of wrong guesses
        self._jumper.draw_jumper(wrong_guesses)
