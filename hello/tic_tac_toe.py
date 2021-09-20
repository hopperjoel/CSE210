
#Tic-tac-toe game for CSE 210

#Author: Joel Hopper

"""
Tic-Tac-Toe is played by two players taking turns selecting
a number (1-9), which represents a position on the game board

The first player to select 3 items in a row (either vertically, horizontally, or diagonally) wins
"""

def main():
    #allow for user input
    #board changes according to input - need to pass through input to function?
    print("Welcome to Tic-Tac-Toe\n")
    player_1_name = input("Please enter player 1 name: ")
    player_2_name = input("Please enter player 2 name: ")
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(f"{player_1_name} will be 'X' and {player_2_name} will be 'O'\n")
    
    selection_func(player_1_name, player_2_name, board)

def selection_func(p1_name, p2_name, board):

    def create_disp_func(board):
    
        mod_board = ("\n" + board[0] + "|" + board[1] + "|" + board[2] + "\n", 
            "-+-+-\n",
            board[3] + "|" + board[4] + "|" + board[5] + "\n",
            "-+-+-\n",
            board[6] + "|" + board[7] + "|" + board[8] + "\n")

        print_board = ""
        for i in mod_board:
            print_board += i
        
        return print_board

    game_go = True
    while game_go:
        p1_select = True
        p2_select = True
        while p1_select:
            p1_choice = int(input(f"{p1_name} Select a square from 1 to 9: "))
            board[p1_choice - 1] = "X"
            player_board = create_disp_func(board)
            print(player_board)
        
            if board.count("X") == 3:
        
                if board[0:3] == ["X", "X", "X"]:
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
                elif board[3:6] == ["X", "X", "X"]:
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
                elif board[6:9] == ["X", "X", "X"]:
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
                elif board[0] == "X" and board[3] == "X" and board[6] == "X":
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
                elif board[1] == "X" and board[4] == "X" and board[7] == "X":
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
                elif board[2] == "X" and board[5] == "X" and board[8] == "X":
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
                elif board[0] == "X" and board[4] == "X" and board[8] == "X":
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
                elif board[2] == "X" and board[4] == "X" and board[6] == "X":
                    print(f"{p1_name} wins\nThank you for playing!")
                    game_go = False
                    p2_select = False
            elif board.count("X") >= 5 or board.count("O") >= 4:
                print("Draw. Game Over\nThank you for playing!")
                game_go = False
                p2_select = False

            p1_select = False
            
        while p2_select:
            p2_choice = int(input(f"{p2_name} Select a square from 1 to 9: "))
            board[p2_choice - 1] = "O"
            player_board = create_disp_func(board)
            print(player_board)

            if board.count("O") == 3:

                if board[0:3] == ["O", "O", "O"]:
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False
                elif board[3:6] == ["O", "O", "O"]:
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False
                elif board[6:9] == ["O", "O", "O"]:
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False
                elif board[0] == "O" and board[3] == "O" and board[6] == "O":
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False
                elif board[1] == "O" and board[4] == "O" and board[7] == "O":
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False
                elif board[2] == "O" and board[5] =="O" and board[8] == "O":
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False
                elif board[0] =="O" and board[4] =="O" and board[8] == "O":
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False
                elif board[2] == "O" and board[4] =="O" and board[6] == "O":
                    print(f"{p2_name} wins\nThank you for playing!")
                    game_go = False

            p2_select = False

if __name__ == "__main__":
    main()