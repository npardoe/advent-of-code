import re
import builtins

class Solver:

    targets = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
    ]

    def Operator(self, file_path):
        input_list = self.read_to_list(file_path)

        min = self._get_min_target_length(self.targets)
        max = self._get_max_target_length(self.targets)

        converted_list = []
        for line in input_list:
            mixed_string = self.make_windows(self.targets, min, max, line)
            line_number = self._get_result(mixed_string)
            print(line_number)
            converted_list.append(line_number)
            
        print("")
        print(converted_list)

        print("")
        print(sum(converted_list))

    def read_to_list(self, file_path):
        with builtins.open(file_path) as file:
            return file.read().split("\n")

    def make_windows(self, target_list, min, max, search):
        terminal_index = len(search) - min
        start = 0
        print("\nLine:  " + search)
        save_search = search
        while start in range(0, terminal_index + 1):
            found = False
            i = min
            while i in range(min, max + 1):
                if ((end := start + i) > len(search)):
                    break
                window = search[start:end]
                print(window)
                if r := self._check_for_match(window, target_list):
                    search = search[:start + 1] + str(r)+ " "*(len(window)-3) + search[end - 1:]
                    found = True
                    break

                else:
                    i += 1

            start += (i - 1 if found else 1)

        print("Strip: " + search)
        return search.replace(" ","")



    def _get_result(self, line):
        if line:
            regex = re.findall("\d", line)
            print("Regex: " + str(regex))
            return (
                int(
                    regex[0] + regex[-1]
                )
            )
            
    def _get_min_target_length(self, target_list):
        min = len(target_list[0])
        for target in target_list:
            if len(target) < min:
                min = len(target)
        return min

    def _get_max_target_length(self, target_list):
        max = len(target_list[0])
        for target in target_list:
            if len(target) > max:
                max = len(target)
        return max
    
    def _check_for_match(self, value, value_list):
        if value in value_list:
            return value_list.index(value) + 1
        else:
            return 0
    
    def _get_sum(self, result_list):
        return sum(result_list)