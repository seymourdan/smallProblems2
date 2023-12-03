import re

'''
Find the numbers in each line of the engine grid. Then check around each number for special characters and return True if any are found.
'''

found_numbers = []

def check_surrounding_chars(grid, x, y, length, width, height):
    for offset in range(length):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= x + offset + i < width and 0 <= y + j < height:
                    if grid[y + j][x + offset + i] != '.' and not grid[y + j][x + offset + i].isdigit():
                        return True
    return False

with open('3input.txt', 'r') as file:
    content = file.read()
    engine = content.split('\n')
    grid = [list(row) for row in engine]
    width = len(engine[0])
    height = len(engine)

    for y, row in enumerate(engine):
            for match in re.finditer(r'\d+', row):
                number = match.group()
                length = len(number)
                x = match.start()
                special_char_found = check_surrounding_chars(grid, x, y, length, width, height)
                found_numbers.append({"number": number, "row": y, "col": x, "special_char_found": special_char_found})


count = 0
for num in found_numbers:
    if num['special_char_found']:
        count += int(num['number'])  # Convert the number to an integer before adding

print("Total sum of numbers with a special character nearby:", count)






