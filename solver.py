import copy

class Grid():

    def __init__(self, grid):
        self.grid = grid

    def find_empty(self):
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == 0:
                    return (row, col)
        return False

    def validate(self, num, row, col):
        # check row
        for i in range(len(self.grid[0])):
            if self.grid[row][i] == num and i != col:
                return False

        #check column
        for i in range(len(self.grid)):
            if self.grid[i][col] == num and i != row:
                return False

        # check box
        box_y = row // 3
        box_x = col // 3

        for i in range(box_y * 3, box_y + 3):
            for j in range(box_x * 3, box_x + 3):
                if self.grid[i][j] == num and (i,j) != (row,col):
                    return False

        return True


    def solve(self, states=[]):
        # solve the sudoku
        empty = self.find_empty()
        if not empty:
            return True, states # You won !

        else:
            row, col = empty

        for num in range(1,10):
            if self.validate(num, row, col):
                self.grid[row][col] = num

                if self.solve(states=states)[0]:
                    states.append(copy.deepcopy(self.grid))

                    return True, states

                self.grid[row][col] = 0
        states.append(copy.deepcopy(self.grid))
        return False, None


unsolved = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
