import os
files = []
found = False
directory = "css_comvoi/wavs"

for filename in os.scandir(directory):
    if filename.is_file():
        files.append(filename.name)

with open("css_comvoi/n_val.txt", "r", encoding="utf-8") as f:
    with open("css_comvoi/n2_val.txt", "w", encoding="utf-8") as f2:
        for line in f:
            for i in range(len(files)):
                lineArr = line.split("|")
                if files[i] == lineArr[1]:
                    f2.write(line)