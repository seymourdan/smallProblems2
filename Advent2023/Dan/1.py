import re
# Replace 'path_to_file.txt' with the actual path to your downloaded file
file_path = 'input.txt'

count = 0
# Open the file and read its contents
with open(file_path, 'r') as file:
   for line in file:
        # Find all sequences of digits in the current line
        numbers = re.findall(r"\d", line)
        first = numbers[0]
        last = numbers[-1]
        combined = first + last
        count += int(combined)

print(count)
