# Set a directory for text data files
import os
from pathlib import Path
datapath = Path('data/')
files_in_datapath = [entry for entry in datapath.iterdir() if entry.is_file()]

#print(files_in_datapath[0].name)



