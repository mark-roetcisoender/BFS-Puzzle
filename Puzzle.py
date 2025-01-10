import heapq

def solve_puzzle(Board, Source, Destination):
    """Takes a 2D puzzle along with a Source and Destination parameter. Returns a list detailing
    the path with the minimum number of moves to travel from Source to Destination. In the puzzle,
    cells with '-' are free for travelling, and cells with '#' are blocked. The function returns
    None if no valid paths exist. It also returns a string detailing the direction of each move
    to get from Source to Destination (U,D,L,R)"""
    # initialize variables to track board dimensions and the current location
    column = Source[1]
    row = Source[0]
    m = len(Board[0])
    n = len(Board)
    # return location if Source and Destination are the same
    if Source == Destination:
        return [Source]
    # initialize a matrix of m * n size to track the cost to move around the board
    cost_arr = [[-1 for i in range(m)] for j in range(n)]
    cost_arr[row][column] = 0

    # initialize a visited location list and a queue to track moves
    visited_loc = [(Source)]
    pq = []
    # add initial moves from Source to queue
    if row > 0 and Board[row - 1][column] != '#':   # move 'up
        heapq.heappush(pq, (1, (row - 1, column)))
    if column > 0 and Board[row][column - 1] != '#': #  move 'left'
        heapq.heappush(pq, (1, (row, column - 1)))
    if row < (n -1) and Board[row + 1][column] != '#': #  move 'down'
        heapq.heappush(pq, (1, (row + 1, column)))
    if column < (m - 1) and Board[row][column + 1] != '#': #  move 'right'
        heapq.heappush(pq, (1, (row, column + 1)))
    prev_cost = 0
    # while there are moves to investigate...
    while len(pq) > 0:
        # pop the next element off the queue, get its info and add to visited locations
        priority, item = heapq.heappop(pq)
        row = item[0]
        column = item[1]
        visited_loc.append((row, column))
        # if the location hasn't been visited, or the current 'path' to get here is cheaper
        # than the previous cheapest path, update cost
        if cost_arr[row][column] == -1 or prev_cost + priority < cost_arr[row][column]:
            cost_arr[row][column] = prev_cost + priority
        # add any valid moves to queue from current location
        if row > 0 and Board[row - 1][column] != '#' and (row-1, column) not in visited_loc: # up
            heapq.heappush(pq, (1, (row - 1, column)))
        if column > 0 and Board[row][column - 1] != '#' and (row, column - 1) not in visited_loc: # left
            heapq.heappush(pq, (1, (row, column - 1)))
        if row < (n -1) and Board[row + 1][column] != '#' and (row + 1, column) not in visited_loc: # right
            heapq.heappush(pq, (1, (row + 1, column)))
        if column < (m - 1) and Board[row][column + 1] != '#' and (row, column + 1) not in visited_loc: # down
            heapq.heappush(pq, (1, (row, column + 1)))
        # find the neighboring node with the lowest cost, and use it to update current node's cost
        # if there are no neighboring nodes with valid costs, continue
        prev_cost = get_min_neighbor((row, column), m, n, cost_arr, 1)
        if prev_cost is None:
            continue
        cost_arr[row][column] = prev_cost + priority

    # if Destination is unreachable, return None
    if cost_arr[Destination[0]][Destination[1]] == -1:
        return None
    # Once all nodes are mapped, start at the Destination node, and use the helper function to
    # find the lowest cost path back to the Source node. The list 'path' holds the locations,
    # and the string 'moves' records the actual moves
    path = []
    moves = ""
    cur_char = ""
    path.append(Destination)
    next_node, cur_char = get_min_neighbor(Destination, m, n, cost_arr, 2)
    moves = moves + cur_char
    while Source not in path:
        path.append(next_node)
        next_node, cur_char = get_min_neighbor(next_node, m, n, cost_arr, 2)
        moves = cur_char + moves
    # reverse the path, truncate moves, and return
    path.reverse()
    moves = moves[1:]
    return path, moves

def get_min_neighbor(node, m, n, cost_arr, mode):
    """helper method to find a location's neighbor with the lowest cost to calculate the node's
    lowest cost as well as backtrack to find the optimal solution once all paths are explored.
    mode=1 to return minimum cost of neighboring nodes, and mode=2 to return the x/y location of
    the minimum cost neighbor, along with a character representing the direction (UDLR)"""
    row = node[0]
    col = node[1]
    cost_up = -1
    cost_down = -1
    cost_right = -1
    cost_left = -1
    # check cost for each neighbor of target location if valid
    if row > 0:  # check up cost
        cost_up = cost_arr[row - 1][col]
    if col > 0: # check left cost
        cost_left =cost_arr[row][col - 1]
    if row < (n -1):  # check down cost
        cost_down = cost_arr[row + 1][col]
    if col < (m - 1):  # check right cost
        cost_right = cost_arr[row][col + 1]
    cost_list = []
    # add any valid costs found to a list, and get the minimum of them
    for i in [cost_left, cost_down, cost_right, cost_up]:
        if i != -1:
            cost_list.append(i)
    if len(cost_list) == 0:
        return None
    cost = min(x for x in cost_list if x != -1)
    # this section tracks the direction of the lowest cost neighbor for finding
    # the optimal path through the puzzle
    return_node = ()
    direction = ""
    if cost == cost_up:
        return_node = (row - 1, col)
        direction = 'D'
    elif cost == cost_left:
        return_node = (row, col - 1)
        direction = "R"
    elif cost == cost_down:
        return_node = (row + 1, col)
        direction = "U"
    elif cost == cost_right:
        return_node = (row, col + 1)
        direction = "L"
    # return either cost, or lowest cost neighbor + direction depending on mode
    if mode == 1:
        return cost
    if mode == 2:
        return return_node, direction

def main():
    """"""
    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
        ]
    puzzle1 = [
        ['-', '#', '-'],
        ['-', '#', '-'],
        ['-', '#', '-']
        ]

    # solve_puzzle(puzzle, (0,2), (2,2))
    print(solve_puzzle(puzzle, (0,0), (4,2)))
    print(solve_puzzle(puzzle1, (0,0), (2,2)))

if __name__ == "__main__":
    main()