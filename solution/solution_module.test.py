'''
Suite of tests for the solution module

Author Daniel Rodriguez
'''

import unittest
from solution_module import SolutionModule
class TestSolutionModuleMethods(unittest.TestCase):
    '''
    Tests of the methods for the SolutionModule
    '''
    def setUp(self):
        self.solution_module = SolutionModule()

    #----------------- Generate visited grid tests ----------------------
    def test_generate_visited_grid(self):
        grid = [
            ['*', '#'],
            ['*', '*']
        ]
        expected_result = [
            [False, True],
            [False, False]
        ]
        result = self.solution_module.generate_visited_grid(grid)
        self.assertEqual(result, expected_result)
    #--------------------------------------------------------------------
    #-------------------- calculate_neighbors tests----------------------
    def test_calculate_neighbors(self):
        row, column = 2, 3
        expected_result = [
            (2, 2),
            (3, 3),
            (2, 4),
            (1, 3)
        ]
        result = self.solution_module.calculate_neighbors(row, column)
        self.assertEqual(result, expected_result)
    #--------------------------------------------------------------------
    #-------------------- is_visited tests-------------------------------
    def test_is_visited(self):
        position = (1, 1)
        visited_grid = [
            [True, False],
            [False, False]
        ]
        result = self.solution_module.is_visited(visited_grid, position)
        self.assertEqual(result, False)
        result = self.solution_module.is_visited(visited_grid, (0, 0))
        self.assertEqual(result, True)
    #--------------------------------------------------------------------
    #-------------------- is_valid_position tests------------------------
    def test_is_valid_position(self):
        position = (0, -1)
        result = self.solution_module.is_valid_position(position, 1, 1)
        self.assertEqual(result, False)
        result = self.solution_module.is_valid_position((0, 0), 2, 2)
        self.assertEqual(result, True)
        result = self.solution_module.is_valid_position((2, 3), 3, 3)
        self.assertEqual(result, False)
    #--------------------------------------------------------------------
    #-------------------- Generate Answer tests--------------------------
    def test_generate_answer_case_one(self):
        '''
        Case One consists in a grid without walls
        '''
        grid = [
            ['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '*']
        ]
        result = self.solution_module.generate_answer(grid)
        self.assertEqual(result, 1)

    def test_generate_answer_case_two(self):
        '''
        Case Two consists in a grid with one wall
        '''
        grid = [
            ['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '#'],
            ['*', '*', '*']
        ]
        result = self.solution_module.generate_answer(grid)
        self.assertEqual(result, 1)

    def test_generate_answer_case_three(self):
        '''
        Case Three consists in a grid of a set of walls
        that create a partition
        '''
        grid = [
            ['*', '*', '*'],
            ['*', '*', '*'],
            ['*', '*', '#'],
            ['*', '#', '*']
        ]
        result = self.solution_module.generate_answer(grid)
        self.assertEqual(result, 2)
    #--------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()