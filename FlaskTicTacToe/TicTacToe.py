from flask import Flask, render_template, request
import math
import random

app = Flask(__name__)

# Initialize the game board as a dictionary
game_board = {1: ' ', 2: ' ', 3: ' ',
              4: ' ', 5: ' ', 6: ' ',
              7: ' ', 8: ' ', 9: ' '}

# route to home page
@app.route("/")
def home():
    return render_template("index.html", game_board=game_board)

@app.route("/make_move", methods=["POST"])
def make_move():
    """
    Handles the request to make a move in the tic-tac-toe game.

    Retrieves the position and AI type from the request form.
    Updates the game board with the player's move.
    Determines the AI's move based on the AI type.
    Updates the game board with the AI's move.
    Checks for a winner after each move.
    Returns the updated game board, winner status, game end status, and AI type to be rendered in the template.
    """
    position = int(request.form["position"])
    ai_type = request.form["ai_type"]
    game_board[position] = 'X'
    winner = winner_checker(game_board)
    if not winner:
        if ai_type == "min_max":
            ai_move = min_max_ai_move(game_board)
        elif ai_type == "alphabeta":
            ai_move = alphabeta_ai_move(game_board)
        elif ai_type == "random":
            ai_move = random_ai_move(game_board)
        game_board[ai_move] = 'O'
        winner = winner_checker(game_board)
    game_end = winner is not None
    return render_template("index.html", game_board=game_board, winner=winner, game_end=game_end, ai_type=ai_type)

@app.route("/reset_game", methods=["POST"])
def reset_game():
    """
    Handles the request to reset the tic-tac-toe game.

    Resets the game board to the initial state.
    Returns the updated game board, winner status, game end status, and AI type to be rendered in the template.
    """
    global game_board
    game_board = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "
    }
    return render_template("index.html", game_board=game_board, winner=None, game_end=False, ai_type="min_max")

# Functions
def show_board(game_board):
    print(f" {game_board[1]} | {game_board[2]} | {game_board[3]} ")
    print("===========")
    print(f" {game_board[4]} | {game_board[5]} | {game_board[6]} ")
    print("===========")
    print(f" {game_board[7]} | {game_board[8]} | {game_board[9]} ")

def winner_checker(game_board):
    winning_combinations = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
                            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
                            (1, 5, 9), (3, 5, 7)]  # diagonals
    for combination in winning_combinations:
        if game_board[combination[0]] == game_board[combination[1]] == game_board[combination[2]] != ' ':
            return game_board[combination[0]]
    if ' ' not in game_board.values():
        return 'tie'
    return None

def user_move(game_board):
    while True:
        try:
            move = int(input("Please make your move: "))
            if move in range(1, 10) and game_board[move] == ' ':
                return move
            else:
                print("Invalid move. Please choose an empty cell (1-9).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def min_max_ai_move(game_board):
    best_score = -math.inf
    best_move = None
    for move in game_board.keys():
        if game_board[move] == ' ':
            game_board[move] = 'O'
            score = min_max(game_board, False)
            game_board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def min_max(game_board, is_maximizing):
    winner = winner_checker(game_board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'O'
                score = min_max(game_board, False)
                game_board[move] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'X'
                score = min_max(game_board, True)
                game_board[move] = ' '
                best_score = min(score, best_score)
        return best_score

def alphabeta_ai_move(game_board):
    best_score = -math.inf
    best_move = None
    for move in game_board.keys():
        if game_board[move] == ' ':
            game_board[move] = 'O'
            score = alphabeta(game_board, -math.inf, math.inf, False)
            game_board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
    return best_move

def alphabeta(game_board, alpha, beta, is_maximizing):
    winner = winner_checker(game_board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'O'
                score = alphabeta(game_board, alpha, beta, False)
                game_board[move] = ' '
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = math.inf
        for move in game_board.keys():
            if game_board[move] == ' ':
                game_board[move] = 'X'
                score = alphabeta(game_board, alpha, beta, True)
                game_board[move] = ' '
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def random_ai_move(game_board):
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


if __name__ == "__main__":
    app.run(debug=True)
