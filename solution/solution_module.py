'''
Contains the necessary code
to implement the solution for
the Robot Problem

Author Daniel Rodriguez
'''

class SolutionModule:
    def generate_visited_grid(self, grid):
        '''
        This method generate a matrix which each
        value is either false or true

            - False if it is a space and it was not touched by the algorithm
            - True if it is a wall or it is a space and was touched by the algorithm
        '''
        visited_grid = []
        for idx_row, row in enumerate(grid):
            visited_grid.append([])
            for element in row:
                if element == '*':
                    visited_grid[idx_row].append(False)
                else:
                    visited_grid[idx_row].append(True)
        
        return visited_grid

    def dfs(self, position):
        '''
        Run the algorithm from the given position
        Position is a tuple (x, y) where x is the row position
        and y the column position
        '''
        pass

    def generate_answer(self):
        '''
        Method that provides an answer to the problem
        '''
        pass