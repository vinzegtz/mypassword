import unittest
import string

from mypassword.password import Password, PasswordLevel


class TestPassword(unittest.TestCase):
    
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

    def test_length_of_password(self):
        password_8_chars = Password()
        password_16_chars = Password(length=16)
        password_32_chars = Password(length=32)
        password_48_chars = Password(length=48)

        self.assertEqual(len(password_8_chars.password), 8)
        self.assertEqual(len(password_16_chars.password), 16)
        self.assertEqual(len(password_32_chars.password), 32)
        self.assertEqual(len(password_48_chars.password), 48)
    
    def test_password_level_one(self):
        password_set = set(Password().password)
        intersections = self.__get_intersections(password_set)

        self.assertGreater(len(intersections['level_one']), 0)
        self.assertSetEqual(intersections['level_two'], set())
        self.assertSetEqual(intersections['level_three'], set())
        self.assertSetEqual(intersections['level_four'], set())
    
    def test_password_level_two(self):
        password_set = set(Password(level=PasswordLevel.TWO).password)
        intersections = self.__get_intersections(password_set)

        self.assertGreater(len(intersections['level_one']), 0)
        self.assertGreater(len(intersections['level_two']), 0)
        self.assertSetEqual(intersections['level_three'], set())
        self.assertSetEqual(intersections['level_four'], set())
    
    def test_password_level_three(self):
        password_set = set(Password(level=PasswordLevel.THREE).password)
        intersections = self.__get_intersections(password_set)

        self.assertGreater(len(intersections['level_one']), 0)
        self.assertGreater(len(intersections['level_two']), 0)
        self.assertGreater(len(intersections['level_three']), 0)
        self.assertSetEqual(intersections['level_four'], set())
    
    def test_password_level_four(self):
        password_set = set(Password(level=PasswordLevel.FOUR).password)
        intersections = self.__get_intersections(password_set)

        self.assertGreater(len(intersections['level_one']), 0)
        self.assertGreater(len(intersections['level_two']), 0)
        self.assertGreater(len(intersections['level_three']), 0)
        self.assertGreater(len(intersections['level_four']), 0)


if __name__ == '__main__':
    unittest.main()