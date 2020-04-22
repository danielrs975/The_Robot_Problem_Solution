'''
InputModule
Contains the necessary code to process the user
input

Author: Daniel Rodriguez
'''

valid_characters = [
    '*', # Space
    '#'  # Wall
]

class InputModule:
    '''
    InputModule class that is going to contain
    the method to process an input
    '''

    def is_valid(cells):
        '''
        Check if the elements contained in the cells are
        valid. This mean that are either: '*' (Spaces) or '#' (Wall)
        '''
        for cell in cells:
            if not cell in valid_characters:
                return False
        return True

    def separate_data(line, separation_token = " "):
        '''
        Use to break the data into pieces using a separation token
        for example:
            1 2 3 4 5 (From line)
            [1, 2, 3, 4, 5] (Data generated)
        '''
        return line.split(separation_token)

    def generate_grid(self, string_grid):
        '''
        Turn the string representation of the grid
        into a python matrix (A two dimensional array)
        '''
        rows = self.separate_data(string_grid, '\n')
        grid = []
        for row in rows:
            cells = self.separate_data(row)
            if self.is_valid(self, cells):
                grid.append(cells)
            else:
                raise ValueError(1)
        
        return grid
