import random

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def print_matrix(matrix):
    for i in range(3):
        for j in range(3):
            print("|", matrix[i][j], end=' |')
        print()
        
print_matrix(matrix)

print("\n")





# Winning conditions
def check_win(matrix):
    player_score = 0   
    
    # Check rows
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            player_score += 10
            print("Player", matrix[i][0], "wins!")
            return True

    # Check columns
    for j in range(3):
        if matrix[0][j] == matrix[1][j] == matrix[2][j]:
            player_score += 10
            print("Player", matrix[0][j], "wins!")
            return True
            
        
            
    # Check diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            player_score += 10
            print("Player", matrix[0][0], "wins!")
            return True
        
     
    if matrix[0][2] == matrix[1][1] == matrix[2][0]:
        player_score += 10
        print("Player", matrix[0][2], "wins!")
        return True
    
    
for i in range(4):  
    print("Enter where you want to insert")
    row = int(input("Enter row number (0-2): "))
    column = int(input("Enter column number (0-2): "))
  
    if matrix[row][column] not in ["X", "O"]:
        matrix[row][column] = "X"
    else:
        print("Cell already occupied! Choose another.")
        continue

    print_matrix(matrix)
    print("\n")
    
    # Check if the player wins
    if check_win(matrix):
        break

    if i == 4:  
        break

    print("Computer's move:")
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)

        if matrix[row][column] not in ["X", "O"]:
            matrix[row][column] = "O"
            break

    print_matrix(matrix)
    print("\n")
    
    # Check if the computer wins 
    if check_win(matrix):
        break

if not check_win(matrix) and i == 3:
    print("It's a tie!")


#making moves according to win probabilities
#update probabilities in runtime

probabilities =[[3,2,3],
                [2,4,2],
                [3,2,3]]




