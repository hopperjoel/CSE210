
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
mod_board = ([board[0] + "|" + board[1] + "|" + board[2] + "\n", 
        "-+-+-\n",
        board[3] + "|" + board[4] + "|" + board[5] + "\n",
        "-+-+-\n",
        board[6] + "|" + board[7] + "|" + board[8] + "\n"]
    )

print_board = ""
for i in mod_board:
    print_board += i

print(print_board)