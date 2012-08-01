

FIELD_WIDTH = 3
FIELD_HEIGHT = 3

class Field:

    def __len__(self):
        return len(self.cells)

    def __getitem__(self, index):
        return self.cells[index]

    def __setitem__(self, index, value):
        self.cells[index] = value

    def row(self, index):
        """Get a list of the objects in row[index]."""
        return list(self.cells[index])

    def col(self, index):
        """Get a list of the objects in col[index]."""
        index = index % width
        return [self.cells[i] for i in range(index, height, width)]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Cells are in row-major order
        self.cells = [' ' for _ in range(width * height)]