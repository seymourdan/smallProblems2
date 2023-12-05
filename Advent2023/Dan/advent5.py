# store every 3 as a tuple, excluding word
   # Construct index using the source and range
   # Is it worth finding max number?

    # for section in parts:
    #     for i in range(0, len(seeds), 3):
    #         if i.isdigit() == True:
import re 
maps = {}
def process_numbers(num_str):
    numbers = [int(x) for x in num_str.split()]
    return [(numbers[i], numbers[i + 1], numbers[i + 2]) for i in range(0, len(numbers), 3) if i+2 < len(numbers)]

with open('input5.txt', 'r') as file:
    content = file.read()
    parts = content.split('\n\n')
    for section in parts:
        # Split each section into key and number string
        key, num_str = section.split(':', 1) if ':' in section else section.split('\n', 1)
        key = key.replace('\n', '')  # Remove newline if present
        seed_string = parts[0].strip("seeds: ").split(' ') 
        maps[key] = process_numbers(num_str)
        maps['seeds'] = [int(x) for x in seed_string]

def findoutput(x, key):
    found = False
    outputs = []
    for y_tuple in maps[key]:
        # Define the range using the second and third elements of the tuple
        range_start = y_tuple[1]
        range_end = range_start + y_tuple[2]

        # Check if 'x' is within the range
        if range_start <= x <= range_end:
            result = y_tuple[0] + (x - range_start)
            outputs.append(result)
            found = True
            break  # Exit the loop once a match is found

    # If 'x' is not found in any range, print 'x'
    if not found:
        outputs.append(x)
    
    return outputs

# List of keys in the order you want to process them
keys = ['seed-to-soil map', 'soil-to-fertilizer map', 'fertilizer-to-water map', 'water-to-light map', 'light-to-temperature map', 'temperature-to-humidity map', 'humidity-to-location map']

final_values = []
# Iterate through each tuple in 'seeds'
for seed in maps['seeds']:
    current_values = [seed]  # Start with the seed value

    # Iterate through each map key
    for key in keys:
        new_values = []
        for x in current_values:
            outputs = findoutput(x, key)
            new_values.extend(outputs) # Collecting all outputs
        current_values = new_values  # Update current values for the next key

    final_values.extend(current_values)

print(min(final_values))

# # Iterate through each tuple in 'seeds'
# for seed in maps['seeds']:
#     outputs = findoutput(seed, 'seed-to-soil map')
#     for x in outputs:
#         outputs = findoutput(x, 'soil-to-fertilizer map')
#             for x in outputs: 
                
#         print(outputs)



    