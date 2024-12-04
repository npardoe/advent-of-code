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

search = "two1nineeightwothreeabcone2threexyzxtwone3four4nineeightseven2zoneight2347pqrstsixteen"

def get_min_taget_length(target_list):
    min = len(target_list[0])
    for target in target_list:
        if len(target) < min:
            min = len(target)
    return min

def get_max_taget_length(target_list):
    max = len(target_list[0])
    for target in target_list:
        if len(target) > max:
            max = len(target)
    return max

def make_windows(target_list, min, max, search):
    terminal_index = len(search) - min
    start = 0
    while start in range(0, terminal_index + 1):
        found = False
        i = min
        while i in range(min, max + 1):
            if ((end := start + i) > len(search)): \
            return search.replace(" ","")
            window = search[start:end]
            if r := check_for_match(window, target_list):
                search = search[:start] + str(r)+ " "*(len(window)-1) + search[end:]
                found = True
                break

            else:
                i += 1

        start += (i if found else 1)
        

def check_for_match(value, value_list):
    if value in value_list:
        return value_list.index(value) + 1
    else:
        return 0