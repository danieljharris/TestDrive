from itertools import permutations, combinations

def my_exec(input, code):
    exec(input + 'global i; i = %s' % code)
    global i
    return i

def getPerms(seed):
    features = [*seed]
    tmp = []
    for i in range(len(features)):
        oc = permutations(features, i + 1)
        for c in oc:
            tmp.append(list(c))
    return tmp

def check(input, code, goal):
    try:
        result = my_exec(input, ''.join(code))

        if result == goal:
            return True
        else:
            return False
    except:
        return False

def checkRules(rules, code):
    for (input, goal) in rules:
        if check(input, code, goal) == False:
            return False
    return True

def TestDrive(seed, rules):
    print("Fueling car...")
    perms = getPerms(seed)

    print("Starting engine...")

    i = 20

    for perm in perms:
        if checkRules(rules, perm):
            print("Winner: ", "".join(perm))

            i = i - 1
            if i == 0:
                break
    

def main():
    # seed = "++--*/%%xxzz"
    seed = "++--*/xxzz"
    # seed = "*xz"

    rules = [
        ("x = 10; z = 10;", 100),
        ("x = 1; z = 10;", 10),
        ("x = 2; z = 40;", 80),
    ]

    TestDrive(seed, rules)

    print("Done!!!")


if __name__ == "__main__":
    main()