# AI-Tic-Tac-Toe

Using the Min-Max Algorithm and Alpha Beta Pruning, this project implements an AI player that plays tic-tac-toe.

## Project Overview:
  The AI Tic Tac Toe project aims to create an interactive Tic Tac Toe game where users can play against different AI players. The project implements two AI algorithms, namely Alpha-Beta Pruning and Minimax, along with a random AI player for comparison. Minimax and Alpha-beta pruning AI, the heuristic function is where the AI looks ahead to future game states and scores them. The score reflects how favorable that state is to the AI (basically the AI favor state it can win and dislike state that it lose). The main difference between the two is that Alpha-beta pruning includes a step where it may prune (ignore) branches of the game tree that it has determined will never be favorites, which can speed up the decision making process.

## Design Decisions:
  AI Player Selection: The project provides three AI player options: Alpha-Beta Pruning AI, Minimax AI, and Random AI. This allows users to choose the level of experience of different AI strategies. The Alpha-Beta Pruning AI and Minimax AI are both unbeatable, but the Alpha-Beta Pruning AI is more efficient and makes fewer calculations, leading to faster gameplay. The Random AI is a simple AI that makes random moves and is easy to beat.

  ** Board Representation **: The Tic Tac Toe game board is represented using a dictionary in Python. Each key-value pair represents a position on the game board where the key is the position on the board and the value is the current symbol ('X', 'O', or an empty space). This representation allows for easy access to the game_board positions and simplifies the implementation of the game logic. (i.e game_board[1] = 'X' represents the top left position on the game_board and game_board[9] = 'O' represents the bottom right position on the game_board). Originally the thought was to use 2D list but after some debating we decided to use dictionary because The dictionary representation simplifies the game logic by providing intuitive access to board positions using keys. It eliminates the need for nested loops or complex indexing required in a 2D list representation
    i.e game_board[1][1] = 'X' represent top left position.
    for row in board:
      for position in row:
          print(position, end=' ')
      print()
  This nested loop structure can become more complex and less readable as the board size increases or when performing operations that require accessing specific positions.
  
  Validation: The implementation include check to validate the user inputs move and ensure it is within the valid range of positions on the game_board. This ensures fair gameplay and prevents invalid moves. Early on in the project, if a player made an invalid move, the AI would still make a move and the game would continue. This was fixed by adding a check to ensure that the player's move is valid before proceeding with the AI's move. 

  Error Handling: The code includes error handling to handle invalid user inputs and prevent unexpected crashes or incorrect behavior during gameplay. This includes checks for invalid user input for the move position and the AI player selection. The code also includes checks to ensure that the AI player does not make a move if the game has already ended or if user make an invalid move. This prevents the AI from making an unnecessary move after the game has ended.

  Random AI Player for Comparison: The inclusion of a random AI player allows users to experience different levels of AI gameplay and understand the difference in strategies employed. This also allows users to compare the performance of the Minimax and Alpha-Beta Pruning AI players against a random AI player. The random AI player is also useful for testing the game logic and ensuring that the game does not crash or behave unexpectedly when the AI makes a move.
    

## Limitations:
  Lack Modularity: The current implementation is procedural and lacks a modular structure. While it functions correctly, the code could benefit from an OOP approach, where game entities (such as the game game_board, players, and AI strategies) are encapsulated within classes, leading to cleaner code organization and easier scalability.
    
    
## Future Improvements:
  Game Statistics: utilizing a database to track and display previous game statistics such as win/loss/tie ratios for each player, allowing users to evaluate their performance over time.
    
  Object-Oriented Programming (OOP):utilize object-oriented programming principles. This can improve code organization, modularity, and maintainability, making it easier to scale and enhance the game in the future.
    
  AI Difficulty: Currently both alpha beta and min_max are unbeatable but a way we can improve this by implementing a random factor to the AI move this will make the AI more fun to play against and less predictable. A possible way to do this is to keep a list of best move and randomly choosing a move from such list or use mean to take the avg move favorable move.



## Report

### Date: 5/19/2023

#### Description

Met and discussed project specifications, deliverables, and initial implementation.

#### Details

The initial implementation of the Tic Tac Toe game was completed. The game board was represented using a simple 2D list. Basic functionalities such as displaying the board, getting user input, and checking for a winner were implemented. At this stage, the game was limited to player vs. player mode, and no AI players were involved in the gameplay. The initial implementation was proposed by Mahmood Sakib and implemented by Quang Le.

### Date: 5/20/2023

#### Description
Changes to the implementation and GitHub repository made.

#### Details

The implementation of the game board representation was changed from a 2D list to a dictionary. This change was proposed by Adam Clark and implemented by Quang Le with the assistance of Mahmood Sakib. The use of a dictionary simplified the access to board positions and improved the efficiency of the code. This modification enhanced the implementation and paved the way for future enhancements, such as the addition of AI players. Additionally, a random AI player was added for comparison. The random AI player was implemented by Quang Le and tested by Adam Clark and Mahmood Sakib by playing against the AI and verifying that the AI makes random moves. Furthermore, a game play loop was created to ask the user if they want to play again. This feature was implemented by Adam Clark and tested by Quang Le and Mahmood Sakib by playing the game, checking if the game asks the user if they want to play again, and resetting the game board by clearing out all dictionary values.

### Date: 5/21/2023

#### Description: 
Minimax AI Implementation and Renaming Variable
    
#### Details: 
The Minimax AI algorithm was implemented. The algorithm was implemented using a recursive approach. At first we ran into a huge infinite recusion loop but after some more research we realize that we never had any terminal state where the recursion would exit which was added by returning the status of the board using winner_checker. The Minimax AI was implemented by Quang Le and tested by Adam Clark by feeding AI the multiple variation of game board and checking if it chooses the correct solution.

### Date: 5/22/2023-5/23/2023

#### Description: 
Validation,Error Handling,Alpha-Beta Pruning AI (ExCred) Implementation and Player Choice for AI, Modularization of Code
    
#### Details: 
The code was updated to include validation and error handling. This includes checks for invalid user input for the move position. The code also includes checks to ensure that the AI player does not make a move if the game has already ended. This prevents the AI from making an unnecessary move after the game has ended. The validation and error handling was implemented by Quang Le and tested by Adam Clark and Mahmood Sakib by playing the game and testing for invalid inputs and unexpected behavior.The Alpha-Beta Pruning AI algorithm was implemented. The algorithm was implemented similarly to Min-Max but now include pruning to eliminate unfavorable outcome by breaking before a score could be return. The algorithm was tested and verified to be working correctly. The Alpha-Beta Pruning AI was implemented by Quang Le and tested by Adam Clark and Mahmood Sakib by playing the game and checking if the AI makes the correct moves by comparing it to the Minimax AI moves and also comparing time it takes to make a decision. The Alpha-Beta Pruning AI was found to be more efficient and faster than the Minimax AI which is expected. Up until this point if we wanted to switch between AI players we would have to manually comment out the code for the AI we don't want to use and uncomment the code for the AI we want to use. This is not ideal so we decided to implement a way for the user to choose which AI they want to play against. This was implemented by Adam Clark and Mahmood Sakib and tested by Quang Le by playing the game and selecting different AI players and verifying that the correct AI player is selected. The final touch up for our code was breaking up the main code into smaller function making it more modular and readable. This was implemented by Adam Clark and tested by Quang Le and Mahmood Sakib by playing the game and verifying that the game still works as intended.

## Resouces
[The Coding Train](https://www.youtube.com/watch?v=trKjYdBASyQ&t=30s)
[Anmol Chandel](https://github.com/anmolchandelCO180309/tic-tac-toe-using-alpha-beta-pruning)

## Contributors
- [Mahmood Sakib](https://github.com/mSakib20)
- [Quang Le](https://github.com/Q-Wrld97)
- [Adam Clark](https://github.com/clarkca7)

