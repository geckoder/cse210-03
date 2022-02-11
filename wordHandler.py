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
    

