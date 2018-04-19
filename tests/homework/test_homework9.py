import unittest
from src.homework.homework9.die import Die

#Write the import statement for the Die class

class TestHomework9(unittest.TestCase):

    def test_rolls_values_1_to_6(self):
        self.dietest = Die()
        self.assertTrue(range(1,6), self.dietest.roll())
        '''
        Write a test case to ensure that the Die class only rolls values from 1 to 6
        '''
if __name__ == '__main__':
    unittest.main()
