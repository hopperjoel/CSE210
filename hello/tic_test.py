


board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
p1_name = "bill"
p2_name = "mom"
game_go = True
while game_go:
        p1_select = True
        p2_select = True
        while p1_select:
            p1_choice = int(input(f"{p1_name} Select a square from 1 to 9: "))
            board[p1_choice - 1] = "X"
            print(board)

            if board.count("X") == 3:
        
                if board[0:3] == ["X", "X", "X"]:
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False
                elif board[3:6] == ["X", "X", "X"]:
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False
                elif board[6:9] == ["X", "X", "X"]:
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False
                elif board[0] == "X" and board[3] == "X" and board[6] == "X":
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False
                elif board[1] == "X" and board[4] == "X" and board[7] == "X":
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False
                elif board[2] == "X" and board[5] == "X" and board[8] == "X":
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False
                elif board[0] == "X" and board[4] == "X" and board[8] == "X":
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False
                elif board[2] == "X" and board[4] == "X" and board[6] == "X":
                    print(f"{p1_name} wins")
                    game_go = False
                    p2_select = False

            
            p1_select = False

            
            
        while p2_select:
            p2_choice = int(input(f"{p2_name} Select a square from 1 to 9: "))
            board[p2_choice - 1] = "O"

            if board[0:3] == ["O", "O", "O"]:
                print(f"{p2_name} wins")
                game_go = False
            elif board[3:6] == ["O", "O", "O"]:
                print(f"{p2_name} wins")
                game_go = False
            elif board[6:9] == ["O", "O", "O"]:
                print(f"{p2_name} wins")
                game_go = False
            elif board[0] == "O" and board[3] == "O" and board[6] == "O":
                print(f"{p2_name} wins")
                game_go = False
            elif board[1] == "O" and board[4] == "O" and board[7] == "O":
                print(f"{p2_name} wins")
                game_go = False
            elif board[2] == "O" and board[5] =="O" and board[8] == "O":
                print(f"{p2_name} wins")
                game_go = False
            elif board[0] =="O" and board[4] =="O" and board[8] == "O":
                print(f"{p2_name} wins")
                game_go = False
            elif board[2] == "O" and board[4] =="O" and board[6] == "O":
                print(f"{p2_name} wins")
                game_go = False

            print(board)
            p2_select = False



