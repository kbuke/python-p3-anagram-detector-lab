class Anagram:
    def __init__(self, word):
        self.word = word
    
    @property
    def word(self):
        return self._word 
    
    @word.setter
    def word(self, word):
        if isinstance(word, str):
            self._word = word
        else:
            print("word needs to be a string")

        
    
    def match(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]
    
    def is_anagram(self, word):
        return sorted(self.word.lower()) == sorted(word.lower())