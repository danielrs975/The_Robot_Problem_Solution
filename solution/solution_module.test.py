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
    #-------------------- Generate Answer tests--------------------------
    #--------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()