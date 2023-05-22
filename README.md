# AI-Tic-Tac-Toe

Using the Min-Max Algorithm and Alpha Beta Pruning, this project implements an AI player that plays tic-tac-toe.

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


## Contributors

- [Mahmood Sakib](https://github.com/mSakib20)
- [Quang Le](https://github.com/Q-Wrld97)
- [Adam Clark](https://github.com/clarkca7)

