# Project Title

The Robot problem -  source code file "main.py"

## Getting Started

### Prerequisites

The program is written in Python (version 3.8.2),
downloaded from https://www.python.org/downloads/


## Design
Includes information about the solution, and the structure of the software.

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

### Installing

First unzip the compressed file and run the following command ```python3 main.py```.

## Running the tests

To run the tests use the following command ```sh python3 testing.py```

### Unit tests

### Validation tests

## Built With

```
python3.8  --version
Python 3.8.2

```

## Versioning

## Authors

### Primary Author

Daniel Rodriguez

## License

This project is licensed under the MIT License - see the license.txt file for details
