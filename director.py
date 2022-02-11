from wordHandler import ProcessWord
from jumper import Jumper
from winner import Winner
from secret_word import SecretWord

# Directs the order of the game play. Calls and imports the other classes


class Director:

    def __init__(self):
        self._jumper = Jumper()
        self.winning = Winner()
        self.secretword = SecretWord()
        self.show_word = ProcessWord(self.secretword)
        
        """
        Maybe we can create a word bank where a 
        word is randomly picked from the list?
        """

    
    def start_game(self):
        print("Hello World!")
        #choose a topic
        self.secretword.type_word()
        #get random word
        # secretword = self.secretword.get_random_word()
        guess = input("Enter a letter: ")
        # print dashes to fill
        # Michelle, can you call your functions here?
        # self.show_word.generateInitialWordDisplay(guess)
        # self.show_word.updateWordDisplay()
        
        #jumper drawing
        self._jumper.draw_jumper(0)
        # winner condition
        self.winning.win()
        
       
       

    # def start_game(self):
    #     """
    #     The while loop will need to be ended when the condition 
    #     for either winning or losing is met, not count :)
    #     """
    #     count = 0
    #     guess = input("Enter a letter: ")
    #     updatedWord = self.word.generateInitialWordDisplay(guess)
    #     while self.is_playing:
    #         # wrong_guesses = 0
    #         self._print_jumper(wrong_guesses)
    #         guess2 = input("Enter a letter: ")
    #         updatedWord = self.word.updateWordDisplay(updatedWord, guess2)
    #         count += 1

    # def _print_jumper(self, wrong_guesses):
    #     # prints the jumper with the argument for the number of wrong guesses
    #     self._jumper.draw_jumper(wrong_guesses)
