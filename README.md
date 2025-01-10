# BFS-Puzzle
Algorithm solving a puzzle using BFS techinques

Parameters:
Board- puzzle like list of lists, containing '-' and '#'- see example below
Source- Initial cell to evaluate (row, column)
Destination- Target cell to find shortest path to from Source (row, column)

Solves a 2D puzzle of 'M' columns and 'N' rows. If a cell is open for navigation, it contains '-'. If it isn't, it contains '#'. The algorithm
finds the path traversing the fewest amount of cells by using a BFS approach. This is accomplished by creating an array the same size as the puzzle,
with each cell initialized to '-1'. From the source cell, all possible moves are added to a queue. The adjacent cells are dequeued and evaluated in the order they were enqueued. The
current cell is evaluated to see if the new cost or it's current cost is cheaper. Any valid, unexplored moves from the current cell are added to the queue. This results in the 
'first layer' of moves being evaluated first, then the 'second layer,' and so on until the destination is reached, or all possible moves are evaluated. The shortest path to the destination, 
as well as the 'moves' it is made up of are then returned. If no paths exist to the destination, None is returned.  

Time Complexity: O(m*n). Each moves has the same 'cost' of one, so moves are dequeued in the order they were added (O(1)). Worst case, the algorithm would traverse all cells in the puzzle,
so TC is O(m*n)

Example: 
    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
        ]

    print(solve_puzzle(puzzle, (0,0), (4,2)))
    Output:
    ([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2)], 'RRRRDDDDLL')
