# Set a directory for text data files
import os
from pathlib import Path
datafolder = 'data/'
datapath = Path(datafolder)
files_in_datapath = [entry for entry in datapath.iterdir() if entry.is_file()]

read_file = datafolder + files_in_datapath[1].name
print(read_file)


# Read each line from text data file

book_dict = {}

with open(read_file, 'r', encoding='utf-8-sig') as reader:
    i = 0
    for line in reader:
        key = "line" + str(i)
        value = line
        book_dict[key] = value
        i += 1

# Write each line back into a new text file with some transformations

write_file = datafolder + 'king-james-2020.txt'

with open(write_file, 'w', encoding='utf-8-sig') as writer:
    for value in book_dict.values():
        writer.write(value.lower())

