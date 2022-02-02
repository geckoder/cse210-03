# Import Word Handler Class From File Named "wordHandler"
from wordHandler import ProcessWord

# Create Main Function
def main():
    # Initialize Class
    """
    Maybe we can create a word bank where a 
    word is randomly picked from the list?
    """
    word = ProcessWord("michelle")

    # Process Guesses
    """
    The while loop will need to be ended when the condition 
    for either winning or losing is met, not count :)
    """
    count = 0
    guess = input("Enter a letter: ")
    updatedWord = word.generateInitialWordDisplay(guess)
    while count != 10:
        guess2 = input("Enter a letter: ")
        updatedWord = word.updateWordDisplay(updatedWord, guess2)
        count += 1


        

# Call Main
if __name__ == "__main__":
    main()