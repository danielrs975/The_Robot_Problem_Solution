# Project Title

The Robot problem -  source code file "main.py"

## Getting Started

### Prerequisites

The program is written in Python (version 3.8.2),
downloaded from https://www.python.org/downloads/

### Installing

First unzip the compressed file and run the following command ```python3 main.py```.

## Design
Includes information about the solution, and the structure of the software.

### Input and Output

#### Sample Input

The input consists in many lines:

- The first one contain two numbers: n, m (Separated by a space). Where n is the number of rows and m the number of columns of the grid.
- Then n lines follows. Each line contain m elements (Separated by a space), each of this element can be either '*' that represents a space or '#' that represents a wall

Example:
```
5 6
* * * * # * 
* * * # * *
* # * # # *
* * * # * *
* # # * # *
```

#### Sample Output

The output consists in a single line with a number r that represents the minimum number of robots needed for the given grid.

Example:
```
3
```

### Solution Proposed
The solution of this problem is based in the use of the Depth First Search(DFS) in its core.

The solution is: Everytime a space is found we start a DFS from that space. This is going to visite all the neighbors of that
space and the neighbors of their neighbors. When the algorithm stops (When there are no other spaces to visit) we add one to
the number of robots needed.

Example

we mark x when we visit a cell 

State:

number_of_robots = 0
```        _ _ _ _ _                            _ _ _ _ _ 
start --->|_|_|_|#|_|          First DFS       |x|x|x|#|_|
          |_|_|_|#|_|  ----------------------> |x|x|x|#|_|  number_of_robots = 1
          |_|_|_|#|_|                          |x|x|x|#|_|

 _ _ _ _ _                                        _ _ _ _ _ 
|x|x|x|#|_| <--- start          Second DFS       |x|x|x|#|x|
|x|x|x|#|_|------------------------------------> |x|x|x|#|x| number_of_robots = 2
|x|x|x|#|_|                                      |x|x|x|#|x|
```

As there is no other not visited cell we finish and report that the minimum number
of robots to cover all the grid is two.

### Design details
For this solution, the software is divided in three importants parts, represent it as three files:

- main.py: provide an interface to allow the user to interact with the solution code.
- input.py: contain all the code necessary to process the input, this mean, input validation.
- solution.py: contain the implementation of the algorithm that provide an answer to the problem of the Robot.

### Hypothetic new requirements

- Now a robot can "destroy" a wall, this mean, that it can go through to a wall, it can be only one wall and only one robot can do it.
- The robot can move diagonally now.

### Solution Version 2 (Taking the last requirement)
For this to work we only have to change the method ```calculate_neighbors``` (Find it in the solution_module.py file) to add the neighbors that are diagonally to the current position.

To reuse the same code we add an additional optional argument call ```move_diagonally``` that is ```True``` if the robot can move diagonal or ```False``` otherwise. We add this argument to the ```generate_answer``` method and the ```dfs``` method. 

## Running the tests

To run the tests use the following commands:

- For the solution module: ```python3 solution/solution_module.test.py```
- For the input module: ```python3 solution/input_module.test.py```

### Unit tests

The unit tests are divided in two scripts, one for each existing module.

- input_module.test.py -------> Tests for the Input Module
- solution_module.test.py ------> Tests for the Solution Module

## Built With

```
python3.8  --version
Python 3.8.2

```

## Versioning
```The Robot Problem-Solution Version 1```

## Authors

### Primary Author

Daniel Rodriguez

## License

This project is licensed under the MIT License - see the license.txt file for details
