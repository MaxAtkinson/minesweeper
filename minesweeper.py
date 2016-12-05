from random import randint

class Board:
    def __init__(self):
        self.zones = []
        for x in range(10):
            self.zones.append([])
            for y in range(10):
                mine = bool(randint(0,1))
                self.zones[x].append(Zone(x, y, bool(mine)))

    def print_board(self, show_mines=False):
        for x in self.zones:
            print ' '.join(repr(y) for y in x)

    def count_adjacent_mines(self):
        # Iterate over board rows
        for i in range(len(self.zones)):
            # Iterate over board columns
            for j in range(len(self.zones)):
                # If the current square isn't a mine
                if not self.zones[i][j].has_mine():
                    # Start counting the ones around it
                    count = 0
                    # Starting with the one before it on the row axis
                    p = i - 1
                    while p <= i + 1:
                        # Then on the column axis
                        q = j - 1
                        while q <= j + 1:
                            # If we're not out of bounds
                            if 0 <= p and p < len(self.zones) and 0 <= q and q < len(self.zones):
                                # Check this square has a mine
                                if self.zones[p][q].has_mine():
                                    # If it does, increment the count to display
                                    count += 1
                            q += 1
                        p += 1
                    # Set the count
                    if count > 0: self.zones[i][j].state = str(count)



class Zone:
    def __init__(self, x, y, mine):
        self.x = x
        self.y = y
        if mine:
            self.state = 'M'
        else:
            self.state = 'O'

    def has_mine(self):
        return self.state == 'M'

    def __repr__(self):
        return str(self.state)

class Game():
    def __init__(self):
        self.board = Board()
        self.board.count_adjacent_mines()
        self.board.print_board()

    def run(self):
        pass


if __name__ == '__main__':
    Game()