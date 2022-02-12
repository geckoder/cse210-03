import random
from this import d

class  SecretWord:
     
    def __init__(self):
        
        self.list_words = []
        self.length_list = 0
        self.user_choose = ""
    
    def type_word(self):
        print("Welcome to this game")
        print()
        print("     1. Animals")
        print("     2. Colors")
        print("     3. Book of Mormon Characters")
        print()
        self.user_choose = int(input("Select a topic (1, 2, or 3): "))
        if self.user_choose == 1:
            self.list_words = ["cat", "dog", "parrot", "tucan", "tiger", "horse"]
            print()
            print("You chose 'Animals'")
        elif self.user_choose == 2: 
            self.list_words = ["red", "orange", "blue", "black", "white", "purple"]
            print()
            print("You chose 'Colors'")
        elif self.user_choose ==3:
            self.list_words = ["moroni", "alma", "mosiah", "jacob", "nephi", "enos"]
            print()
            print("You chose 'Book of Mormon Characters'")
        return self.list_words
          
            
    
    def get_random_word (self):    #Function get a random word from a list
        
        self.length_list = len(self.list_words)     #Find the length of list 
        self.random_word = self.list_words[random.randint(0, self.length_list-1)]
        print(self.random_word)
        
        return self.random_word

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

# Create Class: Handle Secret Word
class ProcessWord():
    # Create Method: Set Secret Word Property
    def __init__(self, secretWord):
        self.secretWord = secretWord


    # Create Method: Accept Secret Word And Change Display
    def generateInitialWordDisplay(self, guess = "none"):
        # Split Word Into Individual Characters
        splitWordArray = [c for c in self.secretWord]
        # Create Variable To Hold Word Length
        wordLength = 0
        # Loop Through Characters, +1 To Word Length
        for character in splitWordArray:
            wordLength += 1
        # Create Array For Display String
        wordString = []
        # Create Variable To Hold Loop Count
        count = 1
        # Loop Through Range of Word Length, Add "__"
        while count <= wordLength:
            wordString.append("__ ")
            count += 1
        # Create Array To Hold Guess (Ex. "a") Index Location
        letterIndexArray = []
        # Find Index Locations of Guess
        if guess != "none":
            # Determine If Guess In Secret Word - Count Represents Working Index
            if guess in self.secretWord:
                count2 = 0
                for letter in splitWordArray:
                    if letter == guess:
                        letterIndex = count2
                        letterIndexArray.append(count2)
                    count2 += 1
        # For Each Instance of Guess In Secret Word, Remove Old Value, Put In Guess Letter
        for index in letterIndexArray:
            wordString.pop(index)
            wordString.insert(index, (guess + " "))
        # Join The Word Together Into One String
        joiner = ""
        joinedWordString = joiner.join(wordString)
        # Display Modified Word
        print(joinedWordString)
        # Store Word (Single String) In Variable
        return joinedWordString


    # Create Method: Update Display of Secret Word
    def updateWordDisplay(self, updatedWord, guess):
        # Split Word Into Individual Characters
        splitWordArray = [c for c in updatedWord]
        # Create Variable To Hold Iteration (Index) Number 
        count = 0
        for character in splitWordArray:
            # Remove Spaces In Word
            if character == " ":
                splitWordArray.pop(count)
            count += 1
        # Remove "_"
        previousCharacter = "placeholder"
        count = 0
        for character in splitWordArray:
            if character == previousCharacter and character == "_":
                splitWordArray.pop(count)
            previousCharacter = character
            count += 1
        # Create Array To Hold Guess Index Value
        foundIndices = []
        count = 0
        # Find Index Associated With Guess Letter
        for character in self.secretWord:
            if character == guess:
                foundIndices.append(count)
            count += 1
        # Remove "__" and Add Guess Letter To Word
        for index in splitWordArray:
            for foundIndex in foundIndices:
                splitWordArray.pop(foundIndex)
                splitWordArray.insert(foundIndex, guess)
        # Make "_" = "__"
        count = 0
        for character in splitWordArray:
            if character == "_":
                splitWordArray.pop(count)
                splitWordArray.insert(count, "__")
            count += 1
        # Join Word Into One String Again
        joiner = " "
        joinedWordString = joiner.join(splitWordArray)
        # Display Updated Word
        print(joinedWordString)
        # Store Updated Word In Variable
        return joinedWordString
    def DetermineIfWrongGuess(self, guess):
        # Split Word Into Individual Characters
        splitWordArray = [c for c in self.secretWord]
        # Create Variable To Hold Iteration (Index) Number 
        count = 0
        for character in splitWordArray:
            # Remove Spaces In Word
            if character == " ":
                splitWordArray.pop(count)
            count += 1
        # Remove "_"
        previousCharacter = "placeholder"
        count = 0
        for character in splitWordArray:
            if character == previousCharacter and character == "_":
                splitWordArray.pop(count)
            previousCharacter = character
            count += 1
        # Create Array To Hold Guess Index Value
        foundIndices = []
        count = 0
        # Find Index Associated With Guess Letter
        wrongGuess = True
        for character in self.secretWord:
            if character == guess:
                wrongGuess = False
            count += 1
        print(wrongGuess)
        return wrongGuess

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


game = SecretWord()
game.type_word()
secretWord = game.get_random_word()
jumperDisplay = Jumper()
wordDisplay = ProcessWord(secretWord)
jumperCount = 0
jumperDisplay.draw_jumper(jumperCount)
updatedWordDisplay = wordDisplay.generateInitialWordDisplay()
count= 0
while count < 10:
    guess = input("Please enter a letter: ")
    updatedWordDisplay = wordDisplay.updateWordDisplay(updatedWordDisplay, guess)
    jumperDisplay.draw_jumper(jumperCount)
    wrongGuess = wordDisplay.DetermineIfWrongGuess(guess)
    if wrongGuess == True:
        jumperCount += 1
    count += 1