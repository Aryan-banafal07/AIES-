input = [[1, 2, " "],
         [4, 5, 3],
         [7, 8, 6]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, " "]]

print("Initial input: \n")
for i in input:
    print(i)

print("\n")

print("Goal input: \n")
for i in goal:
    print(i)

# Hamming distance
def calculate_hamming(input, goal):
    count = 0
    for i in range(len(goal)):
        for j in range(len(goal)):
            if goal[i][j] != input[i][j] and input[i][j] != " ":
                count += 1
    return count

hamming_distance = calculate_hamming(input, goal)
print("\nHamming Distance : ", hamming_distance)

# Find the blank space
def find_blank(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == " ":
                return i, j
    return None 

# Possible moves based on the blank space
def possible_moves(i, j):
    move1 = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
    moves = []
    for m in move1:
        if 0 <= m[0] < len(input) and 0 <= m[1] < len(input[0]):
            moves.append(m)
    return moves

# Swap function to swap blank space with a given move
def swap(input, i, j, move):
    input[i][j], input[move[0]][move[1]] = input[move[0]][move[1]], input[i][j]
    return input

# Check if the current state matches the goal state
def check_goal(input, goal):
    for i in range(len(goal)):
        for j in range(len(goal)):
            if goal[i][j] != input[i][j]:
                return False
    return True

# Traverse and swap until the goal is reached
while not check_goal(input, goal):
    pos = find_blank(input)
    moves = possible_moves(pos[0], pos[1])
    
    
    input = swap(input, pos[0], pos[1], moves[0])
    
    print("\nAfter Swapping: \n")
    for i in input:
        print(i)

    if check_goal(input, goal):
        print("Goal Reached")
        break