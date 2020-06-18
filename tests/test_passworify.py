import unittest
import string

from mypassword.passworify import Passworify

class TestPassworify(unittest.TestCase):
    
    __level_one_chars_set = set(string.ascii_lowercase)
    __level_two_chars_set = set(string.ascii_uppercase)
    __level_three_chars_set = set(string.digits)
    __level_four_chars_set = set(string.punctuation)

    def __get_intersections(self, password_set):
        return {
            'level_one': password_set & self.__level_one_chars_set,
            'level_two': password_set & self.__level_two_chars_set,
            'level_three': password_set & self.__level_three_chars_set,
            'level_four': password_set & self.__level_four_chars_set,
        }

    def test_password_level_four(self):
        string_to_password = 'I want a secure password'
        passworify = Passworify(string_to_password)
        passworify.parse()
        password_set = set(passworify.password.password)
        intersections = self.__get_intersections(password_set)

        self.assertGreater(len(intersections['level_one']), 0)
        self.assertGreater(len(intersections['level_two']), 0)
        self.assertGreater(len(intersections['level_three']), 0)
        self.assertGreater(len(intersections['level_four']), 0)


if __name__ == '__main__':
    unittest.main()