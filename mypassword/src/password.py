import random
import string

class PasswordLevel:
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

class Password:
    def __init__(self, length=8, level=PasswordLevel.ONE):
        self.length = length
        self.level = level
        self.password = self.__get_random_string()
    

    def __str__(self):
        return f'{self.password}'
    

    def __get_random_string(self):
        random_string = []
        available_levels = self.__get_available_levels()

        if self.length < 8:
            raise Exception('The length cannot be less than 8')
        
        for i in available_levels:
            random_string.append(self.__get_level_char(i))

        random.shuffle(random_string)

        for i in range(self.length - self.level):
            next_char_level = random.choice(available_levels)
            random_string.append(self.__get_level_char(next_char_level))

        return ''.join(random_string)
    

    def __get_level_one_char(self):
        return random.choice(string.ascii_lowercase)


    def __get_level_two_char(self):
        return random.choice(string.ascii_uppercase)


    def __get_level_three_char(self):
        return random.choice(string.digits)


    def __get_level_four_char(self):
        return random.choice(string.punctuation)
    

    def __get_level_char(self, level):
        char = ''

        if level == PasswordLevel.ONE:
            char = self.__get_level_one_char()
        elif level == PasswordLevel.TWO:
            char = self.__get_level_two_char()
        elif level == PasswordLevel.THREE:
            char = self.__get_level_three_char()
        elif level == PasswordLevel.FOUR:
            char = self.__get_level_four_char()
        else:
            raise Exception(f'The level {level} does not exists')
        
        return char


    def __get_available_levels(self):
        levels = []

        for i in range(self.level, PasswordLevel.ONE - 1, -1):
            if i == PasswordLevel.ONE:
                levels.append(PasswordLevel.ONE)
            elif i == PasswordLevel.TWO:
                levels.append(PasswordLevel.TWO)
            elif i == PasswordLevel.THREE:
                levels.append(PasswordLevel.THREE)
            elif i == PasswordLevel.FOUR:
                levels.append(PasswordLevel.FOUR)
            else:
                raise Exception(f'The level {i} does not exists')
        
        return list(set(levels))