'''
Main to manually use the solution
for the Robot Problem
author: Daniel Rodriguez
'''
from solution.input_module import InputModule
from solution.solution_module import SolutionModule

if __name__ == '__main__':
    input_module = InputModule()
    solution_module = SolutionModule()
    grid_specification = input()
    grid_specification = grid_specification.split(" ")
    try:
        string_grid = ""
        n, m = int(grid_specification[0]),  int(grid_specification[1])
        if n < 0 or m < 0:
            raise ValueError

        # In here read the first line that does not have any jump line
        line = input()
        string_grid += f'{line}'

        # In here we read the middle lines that must have a jump line
        for i in range(1, n):
            line = input()
            string_grid += f'\n{line}'
        
        grid = input_module.generate_grid(string_grid, m)
        answer = solution_module.generate_answer(grid)
        print(answer)
    except IndexError:
        print("You must provide two numbers")
    except ValueError as error:
        code = error.args[0]
        if code == 1:
            print("Error: Some invalid character inside the grid")
        elif code == 2:
            print("Error: The number of columns are different from the one given")
        else:
            print("Error: The input must be positive integers")