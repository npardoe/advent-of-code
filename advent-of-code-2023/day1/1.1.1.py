import re

class Solver:

    @staticmethod
    def read_to_list(file_path):
        with open(file_path) as file:
            return file.read().split("\n")
        
    def create_result_list(input_list):
        result_list = []
        for line in input_list:
            line += "a"
            result_list.append(int((regex := re.findall("\d", line))[0] + regex[-1]))
        return result_list
    
    def get_sum(result_list):
        return sum(result_list)