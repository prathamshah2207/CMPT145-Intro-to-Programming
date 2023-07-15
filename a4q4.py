# Student Name: Pratham Shah                        Section Number: 01
# NSID: mvr659                                      Course Number: 41442
# Student Number: 11353450                          Instructor: Lauresa Stilling

def MazeReader(m):
    maze_list = []
    file = open(m, 'r')
    for line in file:
        l = []
        for data in line.split():
            l.append(int(data))
        maze_list.append(l)
    return maze_list


def SolveMaze(m, s, g):
    """
    Recursively solve the maze to find a path from the current location to the goal location.

    Arguments:
    - maze: A list of lists representing the maze.
    - current: A tuple (row, column) representing the current location.
    - goal: A tuple (row, column) representing the goal location.

    Returns:
    - True if a path exists from the current location to the goal location, False otherwise.
    """

    # Unpack the start location
    start_row, start_col = s

    # Check if current location is the goal
    if s == g:
        m[start_row][start_col] = 'P'
        return True

    # Check if current location is valid
    if start_row < 0 or start_row >= len(m) or start_col < 0 or start_col >= len(m[0]) or m[start_row][start_col] == 1 or m[start_row][start_col] == 'P':
        return False

    # Mark current location as part of the path
    m[start_row][start_col] = 'P'

    # Recursively explore neighboring cells
    if SolveMaze(m, (start_row - 1, start_col), g) or SolveMaze(m, (start_row, start_col - 1), g) or SolveMaze(m, (start_row + 1, start_col), g) or SolveMaze(m, (start_row, start_col + 1), g):
        return True

    # Backtrack if no path is found
    m[start_row][start_col] = 0
    return False


maze = MazeReader("Maze1.txt")
start = (0, 3)
goal = (4, 5)

print(SolveMaze(maze, start, goal))
for rows in maze:
    for cell in rows:
        print(cell, '', end='')
    print()
