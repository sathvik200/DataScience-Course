import os
file_name = "output.txt"
if not os.path.exists(file_name):
    text = input("Enter text to write to the file:")
    with open(file_name, 'xt') as file:
        file.write(text)
        print("Data successfully written to output.txt.")

text = input("Enter additional text to append:")
with open(file_name, 'at') as file:
    file.write("\n" + text)
    print("Data successfully appended.")

with open(file_name, 'rt') as file:
    lines = file.readlines()
    print("Final content of output.txt:")
    for line in lines:
        print(line.strip())