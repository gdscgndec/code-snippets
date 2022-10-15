simple_color = {0: 'black', 1: 'red', 2: 'blue', 3: 'orange', 4: 'pink', 'g': 'green', 'w': 'brown'}
advance_color = {0: ['black'], 1: ['red', 'red4'], 2: ['blue', 'blue4'], 3: ['orange', 'dark goldenrod'],
                 4: ['pink', 'pink4'], 'g': ['green'], 'w': ['brown']}


class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return '(' + str(self.i) + ',' + str(self.j) + ')'

    def __repr__(self):
        return '(' + str(self.i) + ',' + str(self.j) + ')'

    def __eq__(self, other):
        if self.i == other.i and self.j == other.j:
            return True
        return False

    def is_near(self, other):
        dist = abs(self.i - other.i)
        dist += abs(self.j - other.j)
        if dist < 3:
            return True
        return False

    def dist(self, other):
        return abs(self.i - other.i) + abs(self.j - other.j)

    def __add__(self, other):
        return Vector2D(self.i + other.i, self.j + other.j)
