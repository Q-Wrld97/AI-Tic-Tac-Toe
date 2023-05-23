'''
Project: Project #1 AI Tic Tac Toe
Course: CAP4630 001
Team Members: Adam Clark, Mahmood Sakib, Quang Le
Date: 06/06/2023
'''

import math
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
        if game_board[combination[0]] == game_board[combination[1]] == game_board[combination[2]] != ' ': # If all 3 values are same and not empty
            return game_board[combination[0]]  # Return the winning player's symbol (X or O)

    #  If all spaces are filled and no winner, it's a tie
    if ' ' not in game_board.values():
        return 'tie'

    return None  # Return None if there is no winner yet

# Function to get the user's move
def user_turn(game_board):
    while True:
        try:
            move = int(input("Please make your move: "))  # Get user input for move
            if move in range(1, 10) and game_board[move] == ' ':
                return move  # Return the valid move
            else:
                print("Invalid move please input a valid move")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
# Function to make the AI's move using Minimax
'''
START
|
|--> 1. Start from the root (current board state)
|    |
|    |--> 2. Generate all possible next states
|    |
|    |--> 3. For each state, evaluate using the heuristic function
|    |
|    |--> 4. Select the move with the best heuristic value
|    |
|
|---> 5. Make the move
|
END
'''
def min_max_ai_move(game_board):
    best_score = -math.inf
    best_move = None
    for move in game_board.keys():
        if game_board[move] == ' ':
            game_board[move] = 'O'  # Make a hypothetical move for the AI
            score = min_max(game_board, False)  # Calculate the score using the Minimax algorithm
            game_board[move] = ' '  # Undo the hypothetical move
            if score > best_score:
                best_score = score
                best_move = move
    return best_move  # Return the best move for the AI

# Minimax algorithm
def min_max(game_board, maxing):
    winner = winner_checker(game_board)
    if winner == 'O':
        return 1  # Return 1 if the AI wins
    elif winner == 'X':
        return -1  # Return -1 if the player wins
    elif winner == 'tie':
        return 0  # Return 0 if it's a tie

    if maxing:
        max_score = -math.inf
        for move in game_board.keys():
            if game_board[move] == ' ': # for any empty space
                game_board[move] = 'O'  # Make a hypothetical move for the AI
                score = min_max(game_board, False)  # Recursively call the algorithm for the player's turn
                game_board[move] = ' '  # Undo the hypothetical move
                max_score = max(score, max_score)  # Update the max score
        return max_score  # Return the max score for the AI
    else:
        min_score = math.inf
        for move in game_board.keys():
            if game_board[move] == ' ': # for any empty space
                game_board[move] = 'X'  # Make a hypothetical move for the player
                score = min_max(game_board, True)  # Recursively call the algorithm for the AI's turn
                game_board[move] = ' '  # Undo the hypothetical move
                min_score = min(score, min_score)  # Update the min score
        return min_score  # Return the min score for the player

# Function to make the AI's move using Alpha-Beta Pruning
'''
START
|
|--> 1. Start from the root (current board state)
|    |
|    |--> 2. Generate all possible next states
|    |
|    |--> 3. For each state, evaluate using the heuristic function
|    |     |
|    |     |--> 4. If the heuristic value is less than Alpha, Prune the branch
|    |     |
|    |     |--> 5. Update Beta
|    |
|    |--> 6. Select the move with the best heuristic value
|
|--> 7. Make the move
|
END
'''
def alphabeta_ai_move(game_board):
    best_score = -math.inf
    best_move = None
    for move in game_board.keys():
        if game_board[move] == ' ': # for any empty space
            game_board[move] = 'O'  # Make a hypothetical move for the AI
            score = alphabeta(game_board, -math.inf, math.inf, False)  # Calculate the score using the Alpha-Beta algorithm
            game_board[move] = ' '  # Undo the hypothetical move
            if score > best_score: # if score is better than best score
                best_score = score # Update the best score
                best_move = move # Update the best move
    return best_move  # Return the best move for the AI

# Alpha-Beta Pruning algorithm
def alphabeta(game_board, alpha, beta, maxing):
    winner = winner_checker(game_board)
    if winner == 'O':
        return 1  # Return 1 if the AI wins
    elif winner == 'X':
        return -1  # Return -1 if the player wins
    elif winner == 'tie':
        return 0  # Return 0 if it's a tie

    if maxing:
        max_score = -math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'O'  # Make a hypothetical move for the AI
                score = alphabeta(game_board, alpha, beta, False)  # Recursively call the algorithm for the player's turn
                game_board[move] = ' '  # Undo the hypothetical move
                max_score = max(score, max_score)  # Update the max score
                alpha = max(alpha, max_score) # Update the alpha value with the larger value
                if beta <= alpha: # if beta is less than or equal to alpha prune the tree
                    break
        return max_score  # Return the max score for the AI
    else:
        min_score = math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'X'  # Make a hypothetical move for the player
                score = alphabeta(game_board, alpha, beta, True)  # Recursively call the algorithm for the AI's turn
                game_board[move] = ' '  # Undo the hypothetical move
                min_score = min(score, min_score)  # Update the min score
                beta = min(beta, min_score) # Update the beta value with the smaller value
                if beta <= alpha: # if beta is less than or equal to alpha prune the tree
                    break
        return min_score  # Return the min score for the player

# Function to make the AI's move randomly
'''
START
|
|--> 1. Generate all possible moves
|
|--> 2. Select a random move
|
|--> 3. Make the move
|
END
'''
def random_ai(game_board):
    # Create a list to store available moves
    available_moves = []

    # Iterate over the keys in the game_board dictionary
    for move in game_board.keys():
        # Check if the corresponding value in the game_board is an empty space
        if game_board[move] == ' ':
            # If it is, add the move to the list of available moves
            available_moves.append(move)

    # Use random.choice() to select a random move from the available moves
    return random.choice(available_moves)
  
# Function to ask the player if they want to play another round
def ask_play_again():
    while True:
        play_again = input("Do you want to play another round? Y or N: ")
        if play_again.lower() == 'y':
            return True
        elif play_again.lower() == 'n':
            return False
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")
            
# Function to ask the player for AI player selection
def get_ai_choice():
    while True:
        try:
            ai_choice = int(input("Choose your AI opponent: "))
            if ai_choice in [1, 2, 3]:
                return ai_choice
            else:
                #if choice is not a number between 1 and 3 then print error message and ask again
                print("Invalid choice. Please enter a number between 1 and 3.")
        #if choice is not a number then print error message and ask again
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to play the game
def play():
    while True:
        # Select the AI player
        print(
          "Welcome to Tic Tac Toe You Will Be VS 3 type of AI (your choice) may the force be with you :)!\n"
          "========================================================\n"
          "Game Rules And Instruction:\n"
          "Enter a number from 1-9 to make a move. The number corresponds to the position on the board as shown below.\n"
          "1 | 2 | 3\n"
          "===========\n"
          "4 | 5 | 6\n"
          "===========\n"
          "7 | 8 | 9\n"
          "You will be playing first and your move is X and AI move will be O.\n"
          "========================================================\n"
          "Select the AI player to play against:\n"
          "1. AI with Alpha-Beta Pruning\n"
          "2. AI with Minimax\n"
          "3. Random AI"
          )
        ai_choice = get_ai_choice()
        
        # Reset the game_board for a new game
        game_board = {1: ' ', 2: ' ', 3: ' ', 
                      4: ' ', 5: ' ', 6: ' ',
                      7: ' ', 8: ' ', 9: ' '}

        # Determine the AI move function based on the user's choice
        if ai_choice == 1:
            ai_move_function = alphabeta_ai_move
        elif ai_choice == 2:
            ai_move_function = min_max_ai_move
        else:
            ai_move_function = random_ai
            
        print("""
          Yoda: may the force be with you and good luck young padawan!
       __.-._
       '-._"7'
        /'.-c
        |  /T
        |_)_/
        /  '-. \n
        """)

        # Game loop
        while True:
            # Display the current game board
            show_board(game_board)

            # Get the player's move
            player_move = user_turn(game_board)
            game_board[player_move] = 'X'  # Make the player's move

            # Check for a winner or a tie
            winner = winner_checker(game_board) 
            if winner:
                show_board(game_board)
                if winner == 'tie':
                    print("It's a tie\n")
                elif winner == 'X':
                    print("====================")
                    print("You won\n")
                else:
                    print("====================")
                    print("AI won!\n")
                break

            # Get the AI's move
            ai_move = ai_move_function(game_board)
            game_board[ai_move] = 'O'  # Make the AI's move this is dependent on the earlier choice of AI

            # Check for a winner or a tie
            winner = winner_checker(game_board)
            if winner:
                show_board(game_board)
                if winner == 'tie':
                    print("It's a tie\n")
                elif winner == 'X':
                    print("====================")
                    print("You won\n")
                else:
                    print("====================")
                    print("AI won\n")
                break

        # Ask the player if they want to play another round
        if ask_play_again() == False:
            print("Thank you for playing!\n")
            break
        print("\n")
        
# Main function
if __name__ == "__main__":
    play()