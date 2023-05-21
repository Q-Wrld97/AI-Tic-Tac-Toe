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
    # Printing the game board in a grid form using the values stored in the dictionary
    print(f" {game_board[1]} | {game_board[2]} | {game_board[3]} ")
    print("===========")
    print(f" {game_board[4]} | {game_board[5]} | {game_board[6]} ")
    print("===========")
    print(f" {game_board[7]} | {game_board[8]} | {game_board[9]} ")

# Function to check for a winner
def winner_checker(game_board):
    # List of all possible winning combinations
    winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),  
                            (1, 5, 9), (3, 5, 7)]  

    # Check if any winning combination matches for 'X' or 'O'
    for combination in winning_combinations:
        if game_board[combination[0]] == game_board[combination[1]] == game_board[combination[2]] != ' ': # If all 3 values are same and not empty
            return game_board[combination[0]] 

    # If all spaces are filled and no winner, it's a tie
    if ' ' not in game_board.values():
        return 'tie'

    # If none of the above conditions are met, game continues
    return None  

# Function to get the user's move
def user_turn(game_board):
    # Get move from user as input, validate it and return
    while True:
        try:
            move = int(input("Please make your move: ")) 
            if move in range(1, 10) and game_board[move] == ' ':
                return move  
            else:
                print("Invalid move please input a valid move")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to get the AI player's move
def ai_move(game_board, player):
    while True:
        move = random.randint(1, 9)  # Generate a random move
        if game_board[move] == ' ':
            return move  # Return the valid move
            
# Function to make the AI's move using Minimax
def min_max_ai_move(game_board):
    # Initialize best_score to a very small value
    best_score = -math.inf
    best_move = None
    for move in game_board.keys():
        if game_board[move] == ' ':
            game_board[move] = 'O'  # Temporarily make a move for 'O'
            score = min_max(game_board, False)  # Calculate score for that move
            game_board[move] = ' '  # Undo the move
            # If this score is better than best_score, update best_score and best_move
            if score > best_score:
                best_score = score
                best_move = move
    return best_move  

# Minimax algorithm
def min_max(game_board, is_maximizing):
    # Get the current game status
    winner = winner_checker(game_board)
    # Assign scores if the game is over, based on who has won
    if winner == 'O':
        return 1  
    elif winner == 'X':
        return -1  
    elif winner == 'tie':
        return 0  

    if is_maximizing:  # If this is the maximizing player's turn
        max_score = -math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'O'  # Temporarily make a move
                score = min_max(game_board, False)  # Calculate score for that move
                game_board[move] = ' '  # Undo the move
                # If this score is better than max_score, update max_score
                if score > max_score:
                    max_score = score
        return max_score  
    else:  # If this is the minimizing player's turn
        min_score = math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'X'  # Temporarily make a move
                score = min_max(game_board, True)  # Calculate score for that move
                game_board[move] = ' '  # Undo the move
                # If this score is less than min_score, update min_score
                if score < min_score:
                    min_score = score
        return min_score 

# Function to play the game
def play():
    #reset the game board
    game_board = {1: ' ', 2: ' ', 3: ' ',
                  4: ' ', 5: ' ', 6: ' ', 
                  7: ' ', 8: ' ', 9: ' '}
    print(
          "Welcome to Tic Tac Toe You Will Be VS Min-Max AI \n"
          "========================================================\n"
          "Game Rules And Instruction:\n"
          "Enter a number from 1-9 to make a move. The number corresponds to the position on the board as shown below.\n"
          "1 | 2 | 3\n"
          "===========\n"
          "4 | 5 | 6\n"
          "===========\n"
          "7 | 8 | 9\n"
          "You will be playing first and your move is X and AI move will be O.\n"
          
          )
    print("""
          Yoda: may the force be with you and good luck young padawan!
       __.-._
       '-._"7'
        /'.-c
        |  /T
        |_)_/
        /  '-. \n
        """)
    while True:
        show_board(game_board)
        move = user_turn(game_board)
        game_board[move] = 'X'
        winner = winner_checker(game_board)
        if winner:
            show_board(game_board)
            if winner == 'X':
                print('You won!')
            elif winner == 'O':
                print('AI won!')
                print('AI: That was too ez')
            else:
                print('Its a tie!')
            break

        
        move = min_max_ai_move(game_board)
        game_board[move] = 'O'
        winner = winner_checker(game_board)
        if winner:
            show_board(game_board)
            if winner == 'X':
                print('You won!')
            elif winner == 'O':
                print('AI won!')
                print('AI: That was too ez')
            else:
                print('Its a tie!')
            break 
            
if __name__ == "__main__":
    #play again loop
    while True:
        play()
        play_again = input("Do you want to play another round? Y or N: ").lower()
        if play_again not in ['y', 'yes']:
            break
