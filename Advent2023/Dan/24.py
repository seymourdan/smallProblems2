'''
Go through every combination
Solve each combination and find if the solution is within the bound
'''

from sympy import symbols, Eq, solve
import itertools
import re

data = []
count = 0

with open('24.txt', 'r') as file:
    for row in file:  # Iterate directly over each line in the file
        parts = row.strip().split('@')
        if len(parts) == 2:
            coords_str = parts[0].strip()
            velocities_str = parts[1].strip()

            # Extract numbers from the strings and convert them to integers
            coords = list(map(int, re.findall(r'[-+]?\d+', coords_str)))
            velocities = list(map(int, re.findall(r'[-+]?\d+', velocities_str)))

            data.append([coords, velocities])
        else:
            print(f"Unexpected format in line: {row}")

unique_pairs = list(itertools.combinations(data, 2))
test = ([[366372507252833, 261730973147386, 313848450194648], [-95, 46, 18]], [[190463197800155, 274896788605448, 201892417058162], [194, -845, -304]])

for pair in unique_pairs:
    # Define the symbol for time
    t = symbols('t')

    # Initial positions and velocities
    x1_0, y1_0, z1_0 = pair[0][0]
    v1_x, v1_y, v1_z = pair[0][1]

    x2_0, y2_0, z2_0 = pair[1][0]
    v2_x, v2_y, v2_z = pair[1][1]

    # Parametric equations for each object
    x1 = x1_0 + v1_x * t
    print(x1)
    y1 = y1_0 + v1_y * t
    x2 = x2_0 + v2_x * t
    y2 = y2_0 + v2_y * t

    # Setting up the equations for intersection
    eq1 = Eq(x1, x2)
    print(eq1)
    eq2 = Eq(y1, y2)

    solution = solve((eq1, eq2), t)
    # if 200000000000000<solution<400000000000000:
    #     count +=1 










