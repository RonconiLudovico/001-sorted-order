import unittest

from main import sorted_fun
class Test001(unittest.TestCase):
    def test_sorted_fun(self):
        '''
        test that creates a list in ascending order
        '''
        data1 = [34, 578, 12, 4, 99, 6]
        result1 = sorted_fun(data1)
        self.assertEqual([4, 6, 12,34, 99, 578], result1)

class Test002(unittest.TestCase):
    def test_sorted_fun(self):

        data2 = [454, 23, 45, 66, 887, 9]
        result2 = sorted_fun(data2)
        self.assertEqual([9, 23, 45, 66, 454, 887], result2)

class Test003(unittest.TestCase):
    def test_sorted_fun(self):

        data3 = [999999999, 999999, 99999999999, 99999999]
        result3 = sorted_fun(data3)
        self.assertEqual([999999, 99999999, 999999999, 99999999999], result3)

if __name__ == '__main__':
    unittest.main()
