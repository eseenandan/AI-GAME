# Class for the states of a cell
class State:
    Empty = "-"
    Shaded = "/"


# Game class
class Game:
    def __init__(self, n, players):
        self.grid = [[State.Empty] * n for _ in range(n)]  # initialize grid
        self.players = players  # initialize players

        self.curr_player = 0  # initialize current player
        self.winner = None

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.grid)

    def play(self):
        # play until game is over
        while self.winner is None:
            self.play_turn()
        self.display_board()
        print(f"{self.players[self.winner].symbol} wins!")

    def play_turn(self):
        self.display_board()

        player = self.players[self.curr_player]
        print(f"{player.symbol} to play")

        # get move from current player
        row, col = player.get_move(self.grid)
        print(f"Placing {player.symbol} at {row + 1}, {col + 1}")
        if self.grid[row][col] != "-":
            print("Invalid move!")
            return

        # place symbol on grid
        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i >= 0 and row + i < 6 and col + j >= 0 and col + j < 6:
                    self.grid[row + i][col + j] = State.Shaded
        self.grid[row][col] = player.symbol

        # check if game is over
        self.winner = self.check_winner()
        self.curr_player = (self.curr_player + 1) % 2

    def check_winner(self):
        # if all cells are filled, we have a winner
        if all(cell != State.Empty for row in self.grid for cell in row):
            return self.curr_player
        return None

    def display_board(self):
        print()
        print("    " + "   ".join([str(i + 1) for i in range(len(self.grid))]))
        for i, row in enumerate(self.grid):
            print(f"{i+1}   " + "   ".join(row))
