import re

class Solver():

    def __init__(self, file_path):
        self.base_grid = Solver.read_to_list(file_path)
        self.grid = Solver.standardize(self.base_grid)

    @staticmethod
    def standardize(base_grid):
        grid = []
        for line in base_grid:
            whitespaced = " " + re.sub("[.]", " ", line) + " "
            grid.append(re.sub(r"[^0-9\s]", "*", whitespaced))
        return grid

    @staticmethod
    def read_to_list(file_path):
        with open(file_path) as file:
            return file.read().split("\n")

    class Numer():
        def __init__(self,line, end_index, window, grid):
            self.line = line
            self.start = end_index - len(window) - 1
            self.end = end_index + 1
            self.valid = self._scope(grid)
            self.value = int(window) if self.valid else 0

        def _scope(self, grid):
            grid_scope =   [f"{grid[self.line - 1][self.start:self.end]}",  
                            f"{grid[self.line][self.start:self.end]}",      
                            f"{grid[self.line + 1][self.start:self.end]}"]
            
            passes = False
            for line in grid_scope:
                if "*" in line:
                    passes = True
            return passes
        
    def solvation(self):
        total = 0
        for line, lindex in zip(self.grid, range(0, len(self.grid))):
            window = ""
            for char, chindex in zip(line, range(0, len(line))):
                if char.isdigit():
                    window += char
                    print(window)
                elif window:
                    num = Solver.Numer(lindex,chindex,window,self.grid)
                    print("-> "+self.grid[num.line][num.start + 1:num.end - 1])
                    total += num.value
                    del num
                    window = ""
                else:
                    window = ""
        return total
