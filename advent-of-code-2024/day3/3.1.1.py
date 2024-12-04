def read_to_string(filepath):
    with open(filepath) as file:
        return file.read()

def handler(content):
    total = 0
    arguments = [item.split(")")[0] for item in content.split("mul(") if ")" in item]
    for item in arguments:
        print(item)
        total += check_args(item)
    return total

def check_args(arguments):
    try:
        arguments = arguments.split(",")
        try:
            return int(arguments[0]) * int(arguments[1])
        except:
            return 0
    except:
        return 0

def solver():
    return \
    handler(
        read_to_string("input.txt")
    )

solver()