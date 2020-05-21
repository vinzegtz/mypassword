import random
import string

class Password:
    def __init__(self, length=8):
        self.length = length
        self.password = self.__get_randon_string()
    

    def __str__(self):
        return f'{self.password}'
    

    def __get_randon_string(self):
        random_string = ''

        if self.length < 8:
            raise Exception('The length cannot be less than 8')

        for i in range(self.length):
            random_string += random.choice(string.ascii_lowercase)
        
        return random_string