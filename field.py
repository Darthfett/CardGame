import itertools as it
import card

FIELD_WIDTH = 3
FIELD_HEIGHT = 3

def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return it.zip_longest(*args, fillvalue=fillvalue)

class Field:

    def __delitem__(self, index):
        self.cells[index] = None

    def __getitem__(self, index):
        return self.cells[index]

    def __setitem__(self, index, value):
        self.cells[index] = value

    def __len__(self):
        return len(self.cells)

    def __str__(self):
        rows = ['[' + ']['.join(map(card.repr_for_card, row)) + ']' for row in self.rows()]
        return '\n'.join(rows)

    def col(self, index):
        """Get a list of the objects in col[index]."""
        index = index % width
        return self.cells[index::width]

    def cols(self):
        """Get a list of the columns."""
        return [tuple(self.col(i)) for i in width]

    def row(self, index):
        """Get a list of the objects in row[index]."""
        return self.cells[index * width : (index + 1) * width]

    def rows(self):
        """Get a list of the rows."""
        return list(grouper(3, self.cells))

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Cells are in row-major order
        self.cells = [None for _ in range(width * height)]