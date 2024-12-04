import re

def Operator(file_path):
    input_list = Utilities.read_to_list(file_path)
    output = 0

    check = GameChecker()
    id = 0

    for line in input_list:
        id += 1

        stripped_line = LineParser.strip_line(line)
        tags = LineParser.get_tags(stripped_line)
        values = LineParser.get_values(stripped_line)

        check.director(tags,values)
        check.set_maximums()

        power = 1
        for key in list(check.maximums.keys()):
            power *= check.maximums[key]

        output += power

        check.restore_defaults()
    
    print(output)
    
class Utilities:
    @staticmethod
    def read_to_list(file_path):
        with open(file_path) as file:
            return file.read().split("\n")

class LineParser:

    @staticmethod
    def strip_line(line):
        line = re.sub("\d+(?=:)", "", line)
        line = re.sub("[^0-9dnl]", "", line)
        return line

    def get_values(line):
        values = re.split("[dnl]", line)
        return LineParser._strip_empty_matches(values)

    def get_tags(line):
        tags = re.split("\d", line)
        return LineParser._strip_empty_matches(tags)

    def _strip_empty_matches(listo):
        return list(filter(None,listo))

class GameChecker:

    maximums = {
        "d" : 0,
        "n" : 0,
        "l" : 0,
    }

    tallies = {
        "d" : [],
        "n" : [],
        "l" : [],
    }

    def director(self, tags, values):
        for tag, number in zip(tags,values):
            self.tallies[tag].append(int(number))
        
    # def check_game(self):
    #     over_list = []
    #     for key in list(self.tallies.keys()):
    #         over_list.extend(list(filter(lambda x: x > self.maximums[key], self.tallies[key])))
    #     return False if len(over_list) \
    #     else True

    def set_maximums(self):
        for key in list(self.tallies.keys()):
            for value in self.tallies[key]:
                if value > self.maximums[key]:
                    self.maximums[key] = value
    
    def restore_defaults(self):
        self.tallies = {
        "d" : [],
        "n" : [],
        "l" : [],
        }

        self.maximums = {
        "d" : 0,
        "n" : 0,
        "l" : 0,
    }