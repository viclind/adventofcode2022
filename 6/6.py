import re

stream = open('i.txt').read()
pattern = r'(?=(\w{14}))'
s = [i+14 for i, x in enumerate(re.findall(pattern, stream)) if len(set(x)) == 14][0]
print(s)