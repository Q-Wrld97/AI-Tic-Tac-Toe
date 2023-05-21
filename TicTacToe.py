import random

# Initialize the game game_board as a dictionary
game_board = {1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}

# Function to display the game game_board
def show_board(game_board):
    print(f" {game_board[1]} | {game_board[2]} | {game_board[3]} ")
    print("===========")
    print(f" {game_board[4]} | {game_board[5]} | {game_board[6]} ")
    print("===========")
    print(f" {game_board[7]} | {game_board[8]} | {game_board[9]} ")

# Function to check for a winner
def winner_checker(game_board):
    # Define the winning combinations on the game board
    winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
                            (1, 5, 9), (3, 5, 7)]  # diagonals

    # Check if any of the winning combinations have been achieved by a player
    for combination in winning_combinations:
        if game_board[combination[0]] == game_board[combination[1]] == game_board[combination[2]] != ' ':
            return game_board[combination[0]]  # Return the winning player's symbol (X or O)

    # Check if the game board is full and there is no winner (tie)
    if ' ' not in game_board.values():
        return 'tie'

    return None  # Return None if there is no winner yet

# Function to get the user's move
def user_move(game_board, player):
    while True:
        try:
            move = int(input(f"Player {player}, please make your move: "))  # Get user input for move
            if move in range(1, 10) and game_board[move] == ' ':
                return move  # Return the valid move
            else:
                print("Invalid move. Please input a valid move.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the AI player's move
def ai_move(game_board, player):
    while True:
        move = random.randint(1, 9)  # Generate a random move
        if game_board[move] == ' ':
            return move  # Return the valid move

# Main game loop
def play_game():
    current_player = 'X'  # Start with player X

    while True:
        show_board(game_board)  # Display the game board

        if current_player == 'X':
            move = user_move(game_board, current_player)  # Get the current player's move
        else:
            move = ai_move(game_board, current_player)  # Get the AI player's move
            print(f"AI player chooses position {move}")

        game_board[move] = current_player  # Update the game board with the move

        winner = winner_checker(game_board)  # Check for a winner
        if winner:
            show_board(game_board)  # Display the final game board
            if winner == 'tie':
                print("It's a tie!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch to the other player for the next turn
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
