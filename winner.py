from secret_word import SecretWord
from wordHandler import ProcessWord
from jumper import Jumper


class Winner():
    "Determines if player wins or loses the Jumper Game"

    def __init__(self, secretWord):
        self.complete_word = ProcessWord(secretWord)
        self.right_word = SecretWord()
        self.parachute = Jumper()

    def win(self):
        "Prints statements according to winner or looser condition"
        # Winner condition
        if self.complete_word.secretWord == self.right_word.random_word:
            print('You guessed the word! Have a safe landing!')

        # Looser condition
        elif self.parachute._list == '  x  ':
            print('Your parachute is gone! Call the ambulance!')
