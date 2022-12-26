import sys

from board import Game, State
from solver import AIPlayer, AIPlayerAB, Player


def play(args):
    ai_symbol = "O" if args[0] == "1" else "X"
    player_symbol = "X" if ai_symbol == "O" else "O"

    ai_player = AIPlayerAB(ai_symbol) if args[1] == "AB" else AIPlayer(ai_symbol)
    
    if args[0] == "1":
        players = [ai_player, Player(player_symbol)]
    else:
        players = [Player(player_symbol), ai_player]

    Game(6, players).play()


def generate_stats():
            
    heuristic_code = """
def heuristic(self, board):
    available_moves = [
        (i, j)
        for i in range(len(board))
        for j in range(len(board[i]))
        if board[i][j] == State.Empty
    ]
    return len(board) * len(board[0]) - len(available_moves)
"""
    n = 6
    board = [[State.Empty] * n for _ in range(n)]
    
    with open("readme.txt", "w") as f:
        f.write(heuristic_code + "\n\n")
        f.write("Minmax Algorithm:\n")

        ai = AIPlayer("O", depth=3)
        ai.get_move(board)
        nodes = ai.get_expanded_nodes()

        f.write(f"\tBoard Size - ({n}x{n})\n")
        f.write(f"\tNodes Expanded - {nodes}\n")
        f.write("\tDepth - 3\n\n")

        ai = AIPlayer("O", depth=4)
        ai.get_move(board)
        nodes = ai.get_expanded_nodes()

        f.write(f"\tBoard Size - ({n}x{n})\n")
        f.write(f"\tNodes Expanded - {nodes}\n")
        f.write("\tDepth - 4\n\n\n")
        

        f.write("AB Pruning Algorithm:\n")

        ai = AIPlayerAB("O", depth=3)
        ai.get_move(board)
        nodes = ai.get_expanded_nodes()

        f.write(f"\tBoard Size - ({n}x{n})\n")
        f.write(f"\tNodes Expanded - {nodes}\n")
        f.write("\tDepth - 3\n\n")

        ai = AIPlayerAB("O", depth=4)
        ai.get_move(board)
        nodes = ai.get_expanded_nodes()

        f.write(f"\tBoard Size - ({n}x{n})\n")
        f.write(f"\tNodes Expanded - {nodes}\n")
        f.write("\tDepth - 4\n\n\n")
        


if __name__ == "__main__":
    
    args = sys.argv[1:]
    generate_stats()
    play(args)
