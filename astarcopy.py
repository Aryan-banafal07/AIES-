input = [[1, 2, " "],
         [4, 5, 3],
         [7, 8, 6]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, " "]]

print("Initial State: \n")
for row in input:
    print(row)

print("\nGoal State: \n")
for row in goal:
    print(row)

# Calculate Hamming distance
hamming_distance = 0
for i in range(len(goal)):
    for j in range(len(goal)):
        if goal[i][j] != input[i][j] and input[i][j] != " ":
            hamming_distance += 1

print("\nHamming Distance: ", hamming_distance)

# Traversing (example logic, not A* algorithm)
for i in range(len(goal)):
    for j in range(len(goal)):
        if goal[i][j] != input[i][j]:
            input[i][j] = goal[i][j]

print("\nTraversed State: ")
for row in input:
    print(row)

# Finding blank space
def find_blank(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == " ":
                return i, j
    return None

pos = find_blank(input)
print("\nBlank position: ", pos)

# Move function (template)
# Possible moves: Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move_blank(state, blank_pos, move):
    x, y = blank_pos
    new_x, new_y = x + move[0], y + move[1]
    if 0 <= new_x < 3 and 0 <= new_y < 3:
        new_state = [row[:] for row in state]  # Create a copy of the state
        new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
        return new_state
    return None

# Example of moving the blank space
new_state = move_blank(input, pos, moves[0])  # Try to move up
if new_state:
    print("\nState after moving blank up: ")
    for row in new_state:
        print(row)
else:
    print("\nMove up is not possible.")
