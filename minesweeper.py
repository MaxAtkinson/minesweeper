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
        try:
            x = int(raw_input('Enter an x value : '))
            if x > 9 or x < 0: raise ValueError()
            y = int(raw_input('Enter a y value  : '))
            if y > 9 or y < 0: raise ValueError()
            has_mine = self.board.guess(x, y)
            if has_mine:
                self.render_board(True)
                print 'MINE! You lose.'
            else:
                self.render_board()
                self.turn()
        except:
            print 'Please enter numbers between 0 and 9'
            self.turn()

if __name__ == '__main__':
    Game()