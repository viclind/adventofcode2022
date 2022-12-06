import re
with open("i.txt") as file:
    stream = file.read()
    s = ''.join([i for i in re.findall(r'(?=(\w{14}))', stream) if len(set(i)) == 14][0])
    print(stream.index(s)+14)