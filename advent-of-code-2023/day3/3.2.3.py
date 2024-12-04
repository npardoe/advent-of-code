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

def read_to_list(filepath):
    with open(filepath) as file:
        return _parse_content(file.read())

def _parse_content(content):
    return [re.sub(r"[^0-9.]", "*", line) for line in content.split("\n")]

def custom_slice(iterable, start, end):
    return iterable[max(0,start):end]

def get_neighbors(x, y):
    for r in range(x-1, x+2):
        for c in range(y-1, y+2):
            if min(r,c) >= 0:
                yield r,c

def tokenize_array(grid):
    token_array = []
    for lindex in range(0, len(grid)):
        
        line = grid[lindex]
        token_array.append([])
        window = ""

        for chindex in range(0, len(line)):
            char = line[chindex]

            token_array[lindex].append(0)

            if char.isdigit():
                window += char
            elif window[0:1] not in (".","*","",[]):
                token_array = assign_token(token_array, lindex, chindex, window)
                window = ""
            else:
                if grid[lindex][chindex] == "*":
                    token_array[lindex][chindex] = "*"
                window = ""
    return token_array

def assign_token(token_array, lindex, chindex, window):
    token = int(window)

    for i in range(1, len(window) + 1):
        token_array[lindex][chindex - i] = token

    return token_array

def search_array(token_array):
    total = 0
    for r in range(0, len(token_array)):
        row = token_array[r]
        # print(*line[:50])
        for c in range(0, len(row)):
            column = token_array[r][c]
            if column == "*":
                values = []
                for x,y in get_neighbors(r, c):
                    # values.extend(
                    print(token_array[x][y])
                    # )
                # print(values)
                values = list(filter(lambda x : x and x != "*", values))
                # print(values)
                if len(values) == 2:
                    # print(values[0] * values[1])
                    total += values[0] * values[1]
    return total

def solver():
    return \
    search_array(
        tokenize_array(
            read_to_list("input.txt")
        )
    )

solver()

# Not 89408686
# Not 77377692