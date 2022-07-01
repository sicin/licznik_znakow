from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("./art_pojedyncze"):
    f.extend(filenames)
    break
print(f)
articles = f

# Open file3 in write mode
with open('wszystkie.txt', 'w', encoding="utf-8") as outfile:
    for names in articles:

        # Open each file in read mode
        with open(f"./art_pojedyncze/{names}", encoding="utf-8") as infile:

            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")
