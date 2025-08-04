import math
board = [" " for _ in range(9)]
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")
def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  
        [0,3,6], [1,4,7], [2,5,8],  
        [0,4,8], [2,4,6]            
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False
def is_draw(b):
    return " " not in b
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    elif check_winner(b, "X"):
        return -1
    elif is_draw(b):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
def play():
    print("Tic-Tac-Toe: You (X) vs AI (O)")
    print_board()
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("Invalid move. Try again.")
            continue
        board[move] = "X"
        print_board()
        if check_winner(board, "X"):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")    
            break
        print("AI is thinking...")
        ai_move()
        print_board()
        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
play()
