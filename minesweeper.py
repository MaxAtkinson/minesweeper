from board import Board
from zone import Zone

class Game():
    def __init__(self):
        self.board = Board()
        self.render_board()
        self.turn()

    def render_board(self, show_mines=False):
        self.board.count_adjacent_mines()
        self.board.print_board(show_mines)

    def turn(self):
        x = int(raw_input('Enter an x value : '))
        y = int(raw_input('Enter a y value  : '))
        has_mine = self.board.guess(x, y)
        if has_mine:
            self.render_board(True)
            print 'MINE! You lose.'
        else:
            self.render_board()
            self.turn()


if __name__ == '__main__':
    Game()