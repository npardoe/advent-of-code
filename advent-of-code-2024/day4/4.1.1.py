# test =  [["A1","A2","A3","A4"],
#             ["B1","B2","B3","B4"],
#             ["C1","C2","C3","C4"],
#             ["D1","D2","D3","D4"],]

# # Row - Column
# test1 =  [[0,-1,-2,-3],
#             [1, 0,-1,-2],
#             [2, 1, 0,-1],
#             [3, 2, 1, 0],]

# # Row - Column[::-1]
# test2 = [[-3,-2,-1, 0],
#          [-2,-1, 0, 1],
#          [-1, 0, 1, 2],
#          [ 0, 1, 2, 3],]

# # Row[::-1] - Column[::-1]
# test3 = [[ 0, 1, 2, 3],
#          [-1, 0, 1, 2],
#          [-2,-1, 0, 1],
#          [-3,-2,-1, 0],]

# # Row[::-1] - Column
# test4 = [[3, 2, 1, 0],
#          [2, 1, 0,-1],
#          [1, 0,-1,-2],
#          [0,-1,-2,-3],]

# return [
#     # Front to Back
#     array,

#     # Back to Front
#     [row[::-1] for row in array],

#     # Top to Bottom
#     [[row[column] for row in array] for column in range(0,len(array[0]))],
    
#     # Bottom to Top
#     [[row[column] for row in array[::-1]] for column in range(0,len(array[0]))],

#     # Top Left to Bottom Right
#     self.parse_map(self.map1),
    
#     # Top Right to Bottom Left
#     self.parse_map(self.map2),

#     # Bottom Right to Top Left
#     self.parse_map(self.map3),
    
#     # Bottom Left to Top Right
#     self.parse_map(self.map4),
# ]

import copy

def read_to_list(filepath):
    with open(filepath) as file:
        return file.read().split("\n")
    
class MapMaker():
    def __init__(self, array):
        self.array = array
        self.rows = len(array)
        self.columns = len(array[0])
        self.map1 = [x for x in self._map_gen()]
        # self.map2 = [x for x in self.map_gen(crev=True)]
        # self.map3 = [x for x in self.map_gen(rrev=True,crev=True)]
        self.map4 = [x for x in self._map_gen(rrev=True)]

    def _map_gen(self,rrev=False,crev=False):
        rrev = -1 if rrev else 1
        crev = -1 if crev else 1

        for row in range(0,self.rows)[::rrev]:
            yield [[row,x] for x in range(0,self.columns)[::crev]]

    def _apply_map(self, map):
        """
        Transforms a map into an array of value-mapping tuples
        """
        output = copy.deepcopy(map)
        for r in range(0,len(map)):
            row = map[r]
            for c in range(0, len(row)):
                column = row[c]
                output[r][c] = [self.array[column[0]][column[1]], r - c]
        return output
    
    def _parse_map(self, map):
        """
        Given an array of value-mapping tuples, returns an array of reorganized values
        """
        parsed = []
        for value in range(1 - len(map), len(map)):
            parsed.append([])
            for row in map:
                parsed[value + len(map) - 1].extend([item[0] for item in row if item[1] == value])
        return parsed
    
    def process_maps(self, maps):
        processed = []
        for map in maps:
            processed.append(
                self._parse_map(
                    self._apply_map(
                        map
                    )
                )
            )
        return processed
    
    def collect_maps(self):
        array = self.array
        # Normal (Left to Right maintained)
        maps = [array, [[row[column] for row in array] for column in range(0,len(array[0]))],]
        maps.extend(self.process_maps([self.map1, self.map4]))
        return maps
        
    def print_map(self, map, values=True, mapping=False):
        if values and mapping:
            select = lambda x : [x[0], x[1]]
        elif values:
            select = lambda x : x[0]
        else:
            select = lambda x : x[1]

        for line in map:
            print([select(item) for item in line])

    def search_maps(self,maps):
        total = 0
        for map in maps:
            print("\n" + 50 * "=" + "\n")
            for row in map:
                print(row)
                row_string = "".join(row)
                total += len(row_string.split("XMAS")) - 1
                total += len(row_string.split("SAMX")) - 1
        return total


def solver():
    maker = MapMaker(
        read_to_list("input.txt")
    )
    maps = maker.collect_maps()
    return maker.search_maps(maps)

# test =  [["A1","A2","A3","A4"],
#             ["B1","B2","B3","B4"],
#             ["C1","C2","C3","C4"],
#             ["D1","D2","D3","D4"],]

# input = """\
# 123
# 456
# 789\
# """
# test = input.split("\n")
# print(test)
# maker = MapMaker(test)

# mapped1 = maker.apply_map(maker.map1)
# mapped2 = maker.apply_map(maker.map2)
# mapped3 = maker.apply_map(maker.map3)
# mapped4 = maker.apply_map(maker.map4)

# print(maker.parse_map(mapped1))
# print(maker.parse_map(mapped2))
# print(maker.parse_map(mapped3))
# print(maker.parse_map(mapped4))