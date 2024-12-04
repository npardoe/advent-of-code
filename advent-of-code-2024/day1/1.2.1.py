def read_to_list(filepath):
    with open(filepath) as file:
        return file.read().split("\n")
    
def parse_lists(content):
    list1 = []
    list2 = []
    for line in content:
        list1.append(int(line[:5]))
        list2.append(int(line.strip()[5:]))

    return sorted(list1), sorted(list2)

def find_similarity(lists):
    score = 0
    for num in lists[0]:
        count = 0
        while True:
            try:
                lists[1].remove(num)
            except:
                break
            count += 1
        score += num * count
    return score

def solver():
    return \
    find_similarity(
        parse_lists(
            read_to_list("input.txt")
        )
    )
   