import random


class SecretWord:

    def __init__(self):

        self.list_words = []
        self.lenght_list = 0
        self.user_choose = ""

    def type_word(self):
        print("Welcome to this game")
        print()
        print("     1. Animals")
        print("     2. Colors")
        print("     3. Book of Mormon Characters")
        print()
        self.user_choose = int(input("Select a topic: "))
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
        return self.list_words

    def get_random_word(self):  # Function get a random word from a list

        self.lenght_list = len(self.list_words)  # Find the lenght of list
        self.random_word = self.list_words[random.randint(
            0, self.lenght_list-1)]
        print(self.random_word)

        return self.random_word
