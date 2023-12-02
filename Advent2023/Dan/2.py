import re

max_red = 12 
max_green = 13 
max_blue = 14

count = 0

# Open and read the file
with open('advent2_input.txt', 'r') as file:
    content = file.read()

    # Split content into individual games
    games = content.strip().split('\n')

    # Process each game
    for game in games:
        # Find all occurrences of numbers followed by a color
        
            red_numbers = re.findall(r'(\d+) red', game)
            green_numbers = re.findall(r'(\d+) green', game)
            blue_numbers = re.findall(r'(\d+) blue', game)

            red = max(map(int, red_numbers)) if red_numbers else 0
            green = max(map(int, green_numbers)) if green_numbers else 0
            blue = max(map(int, blue_numbers)) if blue_numbers else 0

            power = red*green*blue
            count += power
    

print(count)
