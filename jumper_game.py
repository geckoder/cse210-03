import random


class SecretWord:
    "Gets a random word from a topic chosen from the player"

    def __init__(self):

        self.list_words = []
        self.length_list = 0
        self.user_choose = ""

    def type_word(self):
        "Asks the user for a topic"
        print("Welcome to the Jumper Game!")
        print()
        print("     1. Animals")
        print("     2. Colors")
        print("     3. Book of Mormon Characters")
        print()
        self.successful_choice = False
        while self.successful_choice == False:
            try:
                self.user_choose = int(input("Select a topic (1, 2, or 3): "))
                self.successful_choice = True
                if self.user_choose == 1:
                    self.list_words = ["cat", "dog",
                                    "parrot", "tucan", "tiger", "horse"]
                    print()
                    print("You chose 'Animals'")
                elif self.user_choose == 2:
                    self.list_words = ["red", "orange",
                                    "blue", "black", "white", "purple"]
                    print()
                    print("You chose 'Colors'")
                elif self.user_choose == 3:
                    self.list_words = ["moroni", "alma",
                                    "mosiah", "jacob", "nephi", "enos"]
                    print()
                    print("You chose 'Book of Mormon Characters'")
                else:
                    print("Try again.")
                    self.successful_choice = False
            except ValueError:
                print("Try again.")
        return self.list_words

    def get_random_word(self):
        "Function get a random word from a list"

        self.length_list = len(self.list_words)  # Find the length of list
        self.random_word = self.list_words[random.randint(
            0, self.length_list-1)]
        # print(self.random_word)

        return self.random_word


class Jumper:
    "Draws jumper with the parachute"

    def __init__(self):
        self._jumper_list = ["  ___  ", " /___\ ", " \   / ",
                             "  \ /  ", "   O   ", "  /|\  ", "  / \  "]
        # Sets a list that draws the jumper

    def draw_jumper(self, wrong_guesses):
        "Shows jumper according to right or wrong guesses"
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
    "Handles the secret word"
    # Create Method: Set Secret Word Property

    def __init__(self, secretWord):
        self.secretWord = secretWord

    # Create Method: Accept Secret Word And Change Display

    def generateInitialWordDisplay(self, guess="none"):
        "Accepts secret word and changes its display"
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
        "Updates and displays secret word"
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
        "Determines if player entered wrong letter, so it does not display"
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
        return wrongGuess


class Result():
    "Determines if player wins or loses the Jumper Game"

    def __init__(self, secret, max_wrong_guesses):
        self.secret = secret
        self.max_wrong_guesses = max_wrong_guesses

    def is_winner(self, word):
        "Check is player wins"
        return word == self.secret

    def is_loser(self, wrong_guesses):
        "Check if player loses"
        return wrong_guesses == self.max_wrong_guesses

    def check_result(self, word, wrong_guesses):
        "Prints if player wins or loses"
        # replaces the space character with an empty string
        formated_word = word.replace(" ", "")
        if self.is_winner(formated_word):
            print()
            print("You guessed the word! Have a safe landing!")
            return True
        elif self.is_loser(wrong_guesses):
            print()
            print("Your parachute is gone! Call the ambulance!")
            return True
        else:
            # if player does not win or lose yet
            return False


game = SecretWord()
game.type_word()
secretWord = game.get_random_word()
jumperDisplay = Jumper()
wordDisplay = ProcessWord(secretWord)
jumperCount = 0
jumperDisplay.draw_jumper(jumperCount)
updatedWordDisplay = wordDisplay.generateInitialWordDisplay()
checker = Result(secretWord, 4)

while True:
    print()
    guess = input("Please enter a letter: ")
    print()
    updatedWordDisplay = wordDisplay.updateWordDisplay(
        updatedWordDisplay, guess)
    wrongGuess = wordDisplay.DetermineIfWrongGuess(guess)
    if wrongGuess == True:
        jumperCount += 1
    # display jumper after each guessed letter
    print()
    jumperDisplay.draw_jumper(jumperCount)

    # break out of loop if player wins or loses
    if checker.check_result(updatedWordDisplay, jumperCount):
        break
