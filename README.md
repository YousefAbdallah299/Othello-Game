# Othello Board Game Project

**Faculty**: Cairo University, Faculty of Computers & Artificial Intelligence  
**Department**: Computer Science  
**Course**: Artificial Intelligence  
**Project**: Othello Board Game

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Game Rules](#game-rules)
3. [Technologies Used](#technologies-used)
4. [Project Features](#project-features)
5. [How to Play](#how-to-play)
6. [Installation](#installation)
7. [Future Improvements](#future-improvements)

---

## Project Overview

This project is a digital implementation of the Othello board game, designed to support Human vs. Computer gameplay using Artificial Intelligence techniques. The computer's decisions are powered by the alpha-beta pruning algorithm, which enhances performance by reducing the number of nodes evaluated in the minimax decision process. This project was developed as part of an Artificial Intelligence course assignment, requiring teams to implement core AI techniques for game strategy and create a user-friendly interface.

## Game Rules

Othello is a two-player strategy game played on an 8x8 grid, using black and white disks:

- Players take turns placing disks with their color facing up, with black moving first.
- Disks are "captured" or flipped to the other color if they are outflanked by two disks of the opposing color in a row, column, or diagonal.
- The game ends when neither player can make a legal move, and the player with the most disks of their color wins.

For more details, you can view the game rules on [eothello.com](https://www.eothello.com/).

## Technologies Used

- **Programming Language**: Python
- **Graphical Interface**: Tkinter
- **Artificial Intelligence**: Alpha-Beta Pruning Algorithm for decision-making
- **Difficulty Levels**: Adjustable by controlling the depth of the search in the alpha-beta pruning (Easy = depth 1, Medium = depth 3, Hard = depth 5)

## Project Features

1. **Game Controller**: Manages player turns, checks move legality, updates the game board, and determines the game end and winner.
2. **Board Representation**: Efficiently tracks and displays board state using Tkinter GUI.
3. **Alpha-Beta Pruning**: Optimized decision-making for the computer player, allowing it to evaluate the best moves while minimizing calculation time.
4. **Difficulty Levels**: Adjustable difficulty by altering the search depth, enhancing the game's challenge.
5. **Human vs. Computer Mode**: Provides an engaging game experience by allowing players to compete against an AI opponent.
6. **Endgame Detection**: Determines game end based on move availability for both players.

## How to Play

1. Launch the game using the Python code provided.
2. The game begins with the board set in the standard Othello starting position.
3. Black always plays first. Click an empty square to place your disk. The computer will respond automatically based on the chosen difficulty.
4. Continue playing until no more legal moves are possible.
5. The player with the majority of disks at the end of the game is declared the winner.


---
