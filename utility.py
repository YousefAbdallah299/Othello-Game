class Utility:
    def checkState(self, board, player1Disks, player2Moves):
        blackCnt = sum(x.count('B') for x in board)
        whiteCnt = sum(x.count('W') for x in board)

        if self.isBoardFull(board) or player1Disks == 0 and not player2Moves:
            if blackCnt > whiteCnt:
                return 'Black Wins'
            if blackCnt == whiteCnt:
                return 'Draw'
            else:
                return 'White Wins'
        return "NONE"

    def evalState(self, computer_symbol, human_symbol, board):
        return sum(x.count(computer_symbol) for x in board) - sum(
            x.count(human_symbol) for x in board)

    def isBoardFull(self, board):
        for x in board:
            if '_' in x:
                return False
        return True
