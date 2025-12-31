import os
file_name = "sample.txt"

if os.path.exists(file_name):
    with open(file_name, 'rt') as f:
        lines = f.readlines()
        print("Reading file content:")
        for line in range(len(lines)):
            print(f"Line {line}: {lines[line].strip()}")
else:
    print(f"Error: The file {file_name} was not found.")