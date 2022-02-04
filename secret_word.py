import random

class  SecretWord:
     
    def __init__(self):
        
        self.list_words = ["word1","word2", "word3", "word4", "word5", "word6"]
        self.lenght_list = 0
    
        
    def get_random_word (self):    #Function get a random word from a list
        
        self.lenght_list = len(self.list_words)     #Find the lenght of list 
        self.random_word = self.list_words[random.randint(0, self.lenght_list-1)]
        

    
