import re

sample = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def read_to_list(file_path):
        with open(file_path) as file:
            return file.read().split("\n")
        
# I want to make a new array replacing each individual string digit with the value of its full number
def tokenize_array(grid):
    compendium = []
    for line, lindex in zip(grid, range(0, len(grid))):
        compendium.append([])
        window = ""
        for char, chindex in zip(line, range(0,len(line))):
            compendium[lindex].append(0)
            if char.isdigit():
                window += char
            elif window:
                token = int(window)
                for i in range(1,len(window) + 1):
                    compendium[lindex][chindex - i] = token
                window = ""
            if char == "*":
                compendium[lindex][chindex] = "*"

    return compendium

def evaluate(compendium):
    total = 0
    for row, outdex in zip(compendium, range(0,len(compendium))):
        print(row)
        for entry, index, in zip(row, range(0,len(row))):
            if entry == "*":
                values = []
                for row in compendium[outdex - 1:outdex + 1]:
                    for item in row[index - 1:index + 1]:
                        try:
                            if item > 0:
                                values.append(item)
                        except: pass
                if len(values) == 2:
                    total += values[0] * values[1]

    return total

def display_compendium(compendium):
    for x in range(0,len(compendium)):
        sthring = ""
        for y in range(0,len(compendium[x])):
            sthring += "[" + str(compendium[x][y]).center(3) + "] "
        print(sthring)

def solve():
    grid = read_to_list("input.txt")
    compendium = tokenize_array(grid)
    display_compendium(compendium)
    print(evaluate(compendium))