from random import randint
from zone import Zone

class Board:
    def __init__(self):
        self.zones = []
        self.no_mines_left = 0
        for x in range(10):
            self.zones.append([])
            for y in range(10):
                mine = bool(randint(0,9) < 1)
                if mine: self.no_mines_left += 1
                self.zones[x].append(Zone(x, y, mine))
        print str(self.no_mines_left) + ' mines left.'

    def print_board(self, show_mines=False):
        if show_mines:
            for x in self.zones:
                print ' '.join(repr(y) for y in x)
        else:
            for x in self.zones:
                print ' '.join(repr(y).replace('M', 'X') for y in x)
        print str(self.no_mines_left) + ' mines in the minefield.'

    def guess(self, x, y):
        self.zones[x][y].uncover()
        if self.zones[x][y].has_mine():
            return True
        return False

    def count_adjacent_mines(self):
        for i in range(len(self.zones)):
            # Iterate over board columns
            for j in range(len(self.zones)):
                # If the current square isn't a mine
                if not self.zones[i][j].has_mine():
                    # Start counting the ones around it
                    count = 0
                    # Starting with the one before it on the row axis
                    for p in range(i-1, i+2):
                        # Then on the column axis
                        for q in range(j-1, j+2):
                            # If we're not out of bounds
                            if p >= 0 and p < len(self.zones) and q >= 0 and q < len(self.zones):
                                # Check this square has a mine
                                if self.zones[p][q].has_mine():
                                    # If it does, increment the count to display
                                    count += 1
                    # Set the count
                    if self.zones[i][j].is_uncovered():
                        if count > 0:
                            self.zones[i][j].state = str(count)
                        else:
                            self.zones[i][j].state = ' '