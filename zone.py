
class Zone:
    def __init__(self, x, y, mine):
        self.x = x
        self.y = y
        self.uncovered = False
        if mine:
            self.state = 'M'
        else:
            self.state = 'X'

    def has_mine(self):
        return self.state == 'M'

    def uncover(self):
        self.uncovered = True

    def is_uncovered(self):
        return self.uncovered

    def __repr__(self):
        if not self.uncovered:
            return 'X'
        return str(self.state)