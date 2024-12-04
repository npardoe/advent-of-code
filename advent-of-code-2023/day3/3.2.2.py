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

def pad_to_list(file_path, pad_char="."):
    with open(file_path) as file:
        content = file.read().split("\n")
        filler_row = (len(content[0]) + 2) * pad_char
        output = [filler_row]
        output.extend(list(map(lambda x : pad_char + x + pad_char, content)))
        output.append(filler_row)
        return output
    
def tokenize_list(grid):
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
            elif window:
                print(token_array)
                coordinates = [lindex,chindex]
                token_array = assign_token(token_array, coordinates, window)
                window = ""


def assign_token(token_array, coordinates, window):
    token = int(window)

    for i in range(1, len(window) - 1):
        token_array[coordinates[0]][coordinates[1 - i]] = token

    return token_array
