
with open('i.txt') as file:
    s = 0
    sums = []
    for line in file:
        if line != '\n':
            s += int(line)
        else:
            sums.append(s)
            s = 0

topThree = sum(sorted(sums, reverse=True)[0:3])

print(str(topThree))
