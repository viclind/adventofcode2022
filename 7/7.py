coms = open("1.txt").read().split("\n")
dirs = []

def next_dir():
    global coms
    if len(coms) == 0:
        return 0
    size = 0
    num_dirs = 1
    i = 1
    row = coms[0]

    if '..' in row:
        return 0
    if 'ls' in row:
        while i < len(coms) and '$' not in coms[i]:
            if not 'dir' in coms[i]:
                size += int(coms[i].split(" ")[0])
            else:
                num_dirs += 1
            i+=1

    for _ in range(0, num_dirs):
        coms = coms[i:]
        size += next_dir()
        i = 1

    if 'cd' in row: dirs.append(size)

    return size

next_dir()
print(sum([dir for dir in dirs if dir <= 100000]))
print([dir for dir in sorted(dirs) if 70000000 - dirs[-1] + dir >= 30000000][0])