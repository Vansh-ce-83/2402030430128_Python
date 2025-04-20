import numpy as np

def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def is_draw(board):
    return not np.any(board == " ")

def main():
    board = np.full((3, 3), " ")
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"\n{player}'s Turn:")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row, col] != " ":
                print("That cell is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        board[row, col] = player
        print_board(board)

        if check_winner(board, player):
            print(f"\n🎉 Player {player} wins!")
            break
        elif is_draw(board):
            print("\nIt's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    main()
