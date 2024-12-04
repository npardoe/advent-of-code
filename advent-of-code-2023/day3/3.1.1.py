import re

# symbols @ # $ % & * - = + /
# line length 140

line1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# read through line
# if digit, start adding to window
# if not digit, check surroundings of window
# if symbol found, commit window
# else discard window

def Operator(string):
    input_list = Utilities.read_string_to_list(string)

    parser = SchematicParser()

    parser.create_parsed_list(input_list)

    for line in parser.parsed_lines:
        print(line)

    parser.make_windows()

    for window in parser.valid_windows:
        print(window)

    print(parser.get_sum(parser.valid_windows))

class Utilities:
    @staticmethod
    def read_file_to_list(file_path):
        with open(file_path) as file:
            return file.read().split("\n")
        
    def read_string_to_list(input_string):
        return input_string.split("\n")
        
class SchematicParser:

    parsed_lines = []
    valid_windows = []

    def create_parsed_list(self, input_list):
        self.parsed_lines.append(" ")
        for line in input_list:
            self.parsed_lines.append(
                self._uniform_symbols(line)
            )
        self.parsed_lines.append(" ")

    def _uniform_symbols(self, line):
        whitespaced = re.sub("[.]", " ", line)
        return re.sub(r"[^0-9.]", "*", whitespaced)
    
    def make_windows(self):
        for line_index in range(1, len(self.parsed_lines) - 1):
            window = ""
            for char_index in range(0, len(self.parsed_lines[line_index])):
                if self.parsed_lines[line_index][char_index].isdigit():
                    window += self.parsed_lines[line_index][char_index]
                    print(window)
                elif (window):
                    if(self.check_window(line_index, char_index - len(window), char_index)):
                        self.valid_windows.append(int(window))
                    window = ""
                    
    def check_window(self, line_num, start, end):
        print("\n")
        for line in range(line_num - 1, line_num + 2):
            # print(f"{line}) " + self.parsed_lines[line][start - 1 : end + 1])
            if "*" in self.parsed_lines[line][start - 1 : end + 1]:
                return True
        return False
    
    def get_sum(self, listo):
        return sum(listo)

        




    