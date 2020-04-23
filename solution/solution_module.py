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

    def calculate_neighbors(self, row, column, can_move_diagonally):
        '''
        Calculate the neighbors cells of a given position

                _|_|_ -----> This is an example of a neighbor cell. The same for the rest. 
                _|x|_
                _|_|_

        '''    
        neighbors_positions = [
            (row, column - 1),
            (row + 1, column),
            (row, column + 1),
            (row - 1, column),
        ]

        if can_move_diagonally:
            neighbors_positions.append((row - 1, column - 1))
            neighbors_positions.append((row - 1, column + 1))
            neighbors_positions.append((row + 1, column - 1))
            neighbors_positions.append((row + 1, column + 1))

        return neighbors_positions

    def is_visited(self, visited_grid, position):
        '''
        Check if a cell is already visited.
        '''
        row = position[0]
        column = position[1]
        return visited_grid[row][column]

    def is_valid_position(self, position, number_rows, number_columns):
        '''
        Check if the coordinates given are
        valid
        '''
        row = position[0]
        column = position[1]
        return ((row >= 0 and row < number_rows) and (column >= 0 and column < number_columns))

    def dfs(self, position, move_diagonally):
        '''
        Run the algorithm from the given position
        Position is a tuple (x, y) where x is the row position
        and y the column position
        '''
        row = position[0]
        column = position[1]
        self.visited_grid[row][column] = True
        neighbors = self.calculate_neighbors(row, column, move_diagonally)
        for neighbor in neighbors:
            if self.is_valid_position(neighbor, self.number_of_rows, self.number_of_columns):
                if not self.is_visited(self.visited_grid, neighbor):
                    self.dfs(neighbor, move_diagonally)


    def generate_answer(self, grid, move_diagonally = False):
        '''
        Method that provides an answer to the problem
        '''
        self.visited_grid = self.generate_visited_grid(grid)
        self.number_of_rows = len(self.visited_grid)
        if (self.number_of_rows == 0):
            return 0
        self.number_of_columns = len(self.visited_grid[0])

        number_of_robots = 0
        for idx_row, row in enumerate(self.visited_grid):
            for idx_column, element in enumerate(row):
                position = (idx_row, idx_column)
                if not self.is_visited(self.visited_grid, position):
                    number_of_robots += 1
                    self.dfs(position, move_diagonally)
    
        return number_of_robots