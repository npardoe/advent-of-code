import re

class Utilities:
    @staticmethod
    def read_file_to_list(file_path):
        with open(file_path) as file:
            return file.read().split("\n")
    
    @staticmethod  
    def read_string_to_list(input_string):
        return input_string.split("\n")
    
    @staticmethod
    def get_sum(listo):
        return sum(listo)
    
class SchematicParser:
    
    parsed_lines = []
    
    def parse_lines(self, input_list):
        for line in input_list:
            self.parsed_lines.append(
                self.standardize(line)
            )

    def standardize(self, line):
        whitespaced = re.sub("[.]", " ", line)
        return re.sub(r"[^0-9\s]", "*", whitespaced)

    def make_windows(self, lines):

        for line_index in range(0, len(lines)):
            window = ""
            for char_index in range(0, len(lines[line_index])):

                if lines[line_index][char_index].isdigit():
                    window += lines[line_index][char_index]
                else:
                    self.check_window(line_index, char_index, window)
                    window = ""

    def check_window(self, line_index, char_index, window):
        assert self.parsed_lines[line_index][char_index - len(window) : char_index] == window
