'''
Suite of tests for the
input module

Author: Daniel Rodriguez
'''
import unittest

from input_module import InputModule

class TestInputModuleMethods(unittest.TestCase):
    '''
    Tests of the methods of the InputModule
    '''
    def setUp(self):
        self.input_module = InputModule()

    #----------------- is_valid method tests ----------------------------
    def test_is_valid_with_valid_values(self):
        cells = ['*', '*', '#', '*']
        result = self.input_module.is_valid(cells)
        self.assertEqual(result, True)

    def test_is_valid_with_wrong_values(self):
        cells = ['*', '1', 2, '#']
        result = self.input_module.is_valid(cells)
        self.assertEqual(result, False)
    #---------------------------------------------------------------------
    #------------------separate_data method tests ------------------------
    def test_separate_data(self):
        line = "* * # * * *"
        expected_result = ['*', '*', '#', '*', '*', '*']
        result = self.input_module.separate_data(line)
        self.assertEqual(result, expected_result)
    #---------------------------------------------------------------------
    #----------------- generate_grid method tests ------------------------
    def test_generate_grid_with_valid_grid(self):
        string_grid = "* * #\n* # *\n* * *"
        expected_result = [
            ['*', '*', '#'],
            ['*', '#', '*'],
            ['*', '*', '*']
        ]
        result = self.input_module.generate_grid(string_grid, 3)
        self.assertEqual(result, expected_result)
    
    def test_generate_grid_with_invalid_grid(self):
        string_grid = "* 1\n* *"
        self.assertRaises(ValueError, self.input_module.generate_grid, string_grid, 2)
    
    def test_generate_grid_with_another_invalid_grid(self):
        string_grid = "* 1\n* *"
        self.assertRaises(ValueError, self.input_module.generate_grid, string_grid, 3)
    #---------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()