import os
import re

folder_path = input("Enter folder path: ")
files = os.listdir(folder_path)

pattern = r"^report.*\.txt$"  # Starts with 'report' and ends with '.txt'

matched_files = [f for f in files if re.match(pattern, f)]
print("Matching .txt files:")
for f in matched_files:
    print(f)
