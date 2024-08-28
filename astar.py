#take input and goal as user input
input = [[1, 2, " "],
         [4, 5, 3],
         [7, 8, 6]]

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, " "]]

print("Intial input: \n")
for i in input:
    print(i)

print("\n")

print("Goal input: \n")
for i in goal:
    print(i)

#hamming distance

count = 0

for i in range(len(goal)):
    for j in range(len(goal)):
        if goal[i][j] != input[i][j] and input[i][j] != " ":
            count += 1

print("\n")

print("Hamming Distance : ", count)


#traversing main logic
#finding blank space

def find_blank(input):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == " ":
                return i, j
    return None 
                


pos=find_blank(input)
print("Blank Spaces index :",pos)


#make possible cases by checking possible moves for index of i and j if one of them is 2 then move

def possible_moves(i, j):
    move1 = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
    moves = []
    for m in move1:
        if 0 <= m[0] < len(input) and 0 <= m[1] < len(input[0]) and input[m[0]][m[1]]!= " ":
            moves.append(m)
            
    return moves

#finding possible moves

moves = possible_moves(pos[0], pos[1])
print("Possible Moves :", moves,"\n")

#swapping with blank space

def swap(input, i, j, move):
    input[pos[0]][pos[1]], input[move[0]][move[1]] = input[move[0]][move[1]], input[pos[0]][pos[1]]
    return input

#testing swap function

for i in input:
    print(i)
 

input = swap(input, pos[0], pos[1], moves[0])

print("\nAfter Swapping: \n")

for i in input:
    print(i)

#check if goal reached

def check_goal(input, goal):
    for i in range(len(goal)):
        for j in range(len(goal)):
            if goal[i][j] != input[i][j]:
                return False
            

if check_goal(input, goal):
    print("Goal Reached")


    


#traversing with swapping 
'''
for i in range(len(goal)):
    for j in range(len(goal)):
        if goal[i][j] != input[i][j]:
            input[i][j] = goal[i][j]

for i in input:
    print(i)
    '''
    
#move func

#move1=[[1,1],[-1,1],[1,-1],[-1,-1]
#move2=[[0,1],[1,0],[-1,0],[0,-1]]


