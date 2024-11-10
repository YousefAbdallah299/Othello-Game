from utility import Utility

emptyToken = '-'


def flip(color):
    if color == 'W':
        return 'B'
    elif color == 'B':
        return 'W'


class GameController:
    def __init__(self, computerToken='$', difficulty=1, twoHumanMode=None):
        self.currY = None
        self.currX = None
        self.computerToken = computerToken
        self.difficulty = difficulty
        self.twoHumanMode = twoHumanMode
        self.board = [[emptyToken for _ in range(8)] for _ in range(8)]
        self.twoHumanMode = False
        self.whitePlayerDisks = 30
        self.blackPlayerDisks = 30
        self.isGameOver = False
        self.canMove = False
        self.whoWins = "NONE"
        self.currentToken = 'B'

        self.board[3][3] = 'W'
        self.board[4][4] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'

    def colorize(self, color, array):
        for i in range(len(array)):
            self.board[array[i][0]][array[i][1]] = color

    def getPlayerDisks(self, color, x=0):
        if color == 'W':
            self.whitePlayerDisks -= x
            return self.whitePlayerDisks
        elif color == 'B':
            self.blackPlayerDisks -= x
            return self.blackPlayerDisks

    def getValidMoves(self, currPlayer):
        moves = []
        for i in range(8):
            for j in range(8):
                if self.isValid(i, j, currPlayer):
                    moves.append([i, j])

        if len(moves) == 0 or self.getPlayerDisks(currPlayer) == 0:
            return []
        return moves

    def isValid(self, x, y, curr_color):
        dx = [+0, +0, -1, +1]
        dy = [-1, +1, +0, +0]

        if self.board[x][y] == 'B' or self.board[x][y] == 'W':
            return []

        opponentIndices = []

        for i in range(4):
            isCurrentIndicesValid = False
            newX = x + dx[i]
            newY = y + dy[i]
            tmp = []

            while 0 <= newX < 8 and 0 <= newY < 8:
                if self.board[newX][newY] != curr_color and self.board[newX][newY] != emptyToken:
                    tmp.append([newX, newY])
                elif self.board[newX][newY] == curr_color and len(tmp) > 0:
                    isCurrentIndicesValid = True
                    break
                elif self.board[newX][newY] == emptyToken:
                    break
                newX += dx[i]
                newY += dy[i]
            if isCurrentIndicesValid:
                for ele in tmp:
                    opponentIndices.append(ele)

        if not opponentIndices:
            return []

        opponentIndices.append([x, y])
        return opponentIndices

    def valid_cell(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] == emptyToken

    def human_play(self, currPlayer):
        if self.isValid(self.currX, self.currY, currPlayer) and self.getPlayerDisks(currPlayer) > 0:
            toBeColored = self.isValid(self.currX, self.currY, currPlayer)
            self.colorize(currPlayer, toBeColored)
            self.board[self.currX][self.currY] = currPlayer

            utility = Utility()
            status = utility.checkState(self.board, self.getPlayerDisks(currPlayer),
                                        self.getValidMoves(flip(currPlayer)))
            if status != "NONE":
                self.isGameOver = True
                self.whoWins = status

            self.currX = -1
            self.currY = -1
            self.getPlayerDisks(currPlayer, 1)
            self.print()
            self.currentToken = flip(currPlayer)
            return True
        else:
            self.currentToken = flip(currPlayer)
            return False

    def computer_play(self):
        x = -1
        y = -1
        print("I AM COMPUTER")
        mx = -float('inf')
        moves = self.getValidMoves(self.computerToken)

        if moves and self.getPlayerDisks(self.computerToken) > 0:
            for move in moves:
                tmpBoard = self.board
                tmp = self.minimax(move[0], move[1], self.difficulty, float('-inf'), float('inf'), 1,
                                   self.computerToken, tmpBoard)
                if mx < tmp:
                    x = move[0]
                    y = move[1]
                    mx = tmp

            toBeColored = self.isValid(x, y, self.computerToken)
            self.colorize(self.computerToken, toBeColored)
            self.board[x][y] = self.computerToken

            utility = Utility()
            status = utility.checkState(self.board, self.getPlayerDisks(self.computerToken),
                                        self.getValidMoves(flip(self.computerToken)))

            if status != "NONE":
                self.isGameOver = True
                self.whoWins = status

            self.getPlayerDisks(self.computerToken, 1)
            self.print()
            self.currentToken = flip(self.computerToken)
            return True
        else:
            self.currentToken = flip(self.computerToken)
            return False

    def minimax(self, x, y, depth, alpha, beta, maxPlayer, currPlayer, board):
        ut = Utility()
        status = ut.checkState(self.board, self.getPlayerDisks(currPlayer), self.getValidMoves(flip(currPlayer)))

        if depth == 0 or status == "NONE":
            if self.computerToken == 'B':
                return ut.evalState('B', 'W', self.board)
            return ut.evalState('W', 'B', self.board)

        if maxPlayer:
            maxEval = -float('inf')
            childs = self.getValidMoves(currPlayer)
            nextPlayer = 'B'
            if currPlayer == 'B':
                nextPlayer = 'W'
            for child in childs:
                eval = self.minimax(child[0], child[1], depth - 1, alpha, beta, not maxPlayer, nextPlayer, board)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
            return maxEval

        else:
            minEval = float('inf')
            childs = self.getValidMoves(currPlayer)
            nextPlayer = 'B'
            if currPlayer == 'B':
                nextPlayer = 'W'
            for child in childs:
                eval = self.minimax(child[0], child[1], depth - 1, alpha, beta, not maxPlayer, nextPlayer, board)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if alpha >= beta:
                    break
            return minEval

    def print(self):
        print("  ", end=" ")
        for col in range(8):
            print(col, end="  ")
        print()

        for row in range(8):
            print(row, end="  ")
            for col in range(8):
                print(self.board[row][col], end="  ")
            print()


game = GameController()
game.print()
