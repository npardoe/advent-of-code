def read_to_string(filepath):
    with open(filepath) as file:
        return file.read()

def handler(content):
    total = 0
    whether = True
    arguments = [[item.split(")")[0],item[len(item.split(")")[0]):]] for item in content.split("mul(") if ")" in item]
    for item, condition in arguments:
        
        print(f"\n{item.ljust(10)}{condition}")

        if whether:
            total += check_args(item)
            print(check_args(item))
        else:
            print(f">{check_args(item)}")
        
        if whether != evaluate_condition(condition, whether):
            whether = evaluate_condition(condition, whether)
            print("\n" + 20 * "=" + f"{whether}" + 20 * "=" + "\n")
    return total

def check_args(arguments):
    try:
        arguments = arguments.split(",")
        try:
            # print(f"{int(arguments[0])} * {int(arguments[1])}")
            return int(arguments[0]) * int(arguments[1])
        except:
            return 0
    except:
        return 0
    
def evaluate_condition(condition,whether):
    dondex = condition.rfind("do(")
    dontdex = condition.rfind("don't(")
    
    if dondex == dontdex:
        return whether
    elif dondex > dontdex:
        return True
    elif dondex < dontdex:
        return False

def solver():
    return \
    handler(
        read_to_string("input.txt")
    )

solver()

# Not 35945650
# Not 67643207