import math

from board import State


# Class for the Player
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = "Player 1" if symbol == "O" else "Player 2"

    # Get the next move from the user
    def get_move(self, board):
        return int(input("Enter row: ")) - 1, int(input("Enter col: ")) - 1


class AIPlayer(Player):
    def __init__(self, symbol, depth=4):
        super().__init__(symbol)
        self.depth = depth
        self.expanded_nodes = 0  # number of expanded nodes in the last get_move

    # get number of expanded nodes
    def get_expanded_nodes(self):
        return self.expanded_nodes

    # Get the next move from the AI
    def get_move(self, board):
        self.expanded_nodes = 0
        _, move = self.minimax(board, self.depth, True)
        return move

    # Minimax algorithm
    def minimax(self, board, depth, is_maximizing):
        self.expanded_nodes += 1
        # Base case: terminal state
        if depth == 0:
            util = self.heuristic(board)
            if is_maximizing:
                return -util, None
            return util, None

        # if game is over
        if all(cell != State.Empty for row in board for cell in row):
            if is_maximizing:
                return -1, None
            return 1, None

        # get all available moves
        available_moves = [
            (i, j)
            for i in range(len(board))
            for j in range(len(board[i]))
            if board[i][j] == State.Empty
        ]
        
        # if maximizing player
        if is_maximizing:
            best_value = -math.inf
            best_move = (-1, -1)
            # find the best move
            for row, col in available_moves:
                value, move = self.minimax(self.apply_move(board, row, col), depth - 1, False)
    
                best_value = max(best_value, value)
                if best_value == value:
                    best_move = (row, col)

            return best_value, best_move

        # if not maximizing player
        best_value = math.inf
        best_move = (-1, -1)
        # find the best move
        for row, col in available_moves:
            value, move = self.minimax(self.apply_move(board, row, col), depth - 1, True)
            best_value = min(best_value, value)
            if best_value == value:
                best_move = (row, col)
        return best_value, best_move

    # Apply a move to the board
    def apply_move(self, board, row, col):
        new_board = [[cell for cell in row] for row in board]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i >= 0 and row + i < 6 and col + j >= 0 and col + j < 6:
                    new_board[row + i][col + j] = State.Shaded
        return new_board

    # Evaluation method
    def heuristic(self, board):
        available_moves = [
            (i, j)
            for i in range(len(board))
            for j in range(len(board[i]))
            if board[i][j] == State.Empty
        ]
        return len(board) * len(board[0]) - len(available_moves)


# AIPlayer with alpha beta pruning
class AIPlayerAB(AIPlayer):
    def __init__(self, symbol, depth=4):
        super().__init__(symbol, depth)

    def get_move(self, board):
        self.expanded_nodes = 0  # reset expanded nodes
        _, move = self.minimaxAB(board, self.depth, True, -math.inf, math.inf)
        return move

    # Minimax algorithm with alpha beta pruning
    def minimaxAB(self, board, depth, is_maximizing, alpha, beta):
        self.expanded_nodes += 1
        # Base case: terminal state
        if depth == 0:
            util = self.heuristic(board)
            if is_maximizing:
                return -util, None
            return util, None

        # if game is over
        if all(cell != State.Empty for row in board for cell in row):
            if is_maximizing:
                return -1, None
            return 1, None

        # get all available moves
        available_moves = [
            (i, j)
            for i in range(len(board))
            for j in range(len(board[i]))
            if board[i][j] == State.Empty
        ]
        # if maximizing player
        if is_maximizing:
            best_value = -math.inf
            best_move = (-1, -1)
            # find the best move
            for row, col in available_moves:
                value, move = self.minimaxAB(self.apply_move(board, row, col), depth - 1, False, alpha, beta)
                best_value = max(best_value, value)
                
                # alpha beta pruning
                alpha = max(alpha, best_value)
                if best_value == value:
                    best_move = (row, col)
                if beta <= alpha:
                    break
            return best_value, best_move

        # if not maximizing player
        best_value = math.inf
        best_move = (-1, -1)
        # find the best move
        for row, col in available_moves:
            value, move = self.minimaxAB(self.apply_move(board, row, col), depth - 1, True, alpha, beta)
            best_value = min(best_value, value)
            
            # alpha beta pruning
            beta = min(beta, best_value)
            if best_value == value:
                best_move = (row, col)
            if beta <= alpha:
                break
        return best_value, best_move
