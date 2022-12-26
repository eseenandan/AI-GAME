
def heuristic(self, board):
    available_moves = [
        (i, j)
        for i in range(len(board))
        for j in range(len(board[i]))
        if board[i][j] == State.Empty
    ]
    return len(board) * len(board[0]) - len(available_moves)


Minmax Algorithm:
	Board Size - (6x6)
	Nodes Expanded - 24597
	Depth - 3

	Board Size - (6x6)
	Nodes Expanded - 428613
	Depth - 4


AB Pruning Algorithm:
	Board Size - (6x6)
	Nodes Expanded - 1411
	Depth - 3

	Board Size - (6x6)
	Nodes Expanded - 21350
	Depth - 4


