import sys
import string
from collections import defaultdict
from os import walk

conc_file = "wszystkie.txt"
f = []
for (dirpath, dirnames, filenames) in walk("./art_pojedyncze"):
    f.extend(filenames)
    break
print(f)

articles = f

with open(conc_file, 'w', encoding="utf-8") as outfile:
    for names in articles:
        with open(f"./art_pojedyncze/{names}", encoding="utf-8") as infile:
            outfile.write(infile.read())
        outfile.write("\n")

try:
    f = open(conc_file, "r", encoding='gbk')
    allstr = f.read()
except UnicodeDecodeError:
    f = open(conc_file, "r", encoding='utf-8')
    allstr = f.read()

# dict to count chars, default to zero
d = defaultdict(int)
for i in allstr:
    d[i] += 1

# count how many dinstinct words
#import jieba
# for i in jieba.cut(allstr):
#    d[i]+=1

# one pass filter, you can just use this filter
for c in string.printable:
    d.pop(c, 0)

# select chinese characters directly
unicode_ranges = [0x3007, 0x3007], [0x3400, 0x4DBF], [
    0x4E00, 0x9FEF], [0x20000, 0x2EBFF]
for i, key in list(enumerate(d)):
    if not any(map(lambda x: x[0] <= ord(key) <= x[1], unicode_ranges)):
        del d[key]
print(f"Tekst: {conc_file[:-4]}")
print(f"Łączna liczba chińskich znaków = {len(d)}")

# map word_count to list of chars
d2 = defaultdict(list)
for key, val in d.items():
    d2[val].append(key)

# sort by val
for key, val in sorted(d2.items(), key=lambda x: x[0], reverse=True):
    print(key, val)
