import numpy as np
def main():
    with open("Advent2023\Lamb\day24.txt") as file:
        lines = file.readlines()
        positions = []
        velocities = []
        count = 0
        for line in lines:
            components = line.strip("\n").split("@")
            coordinates = components[0].split(",")
            speed = components[1].split(",")
            positions.append(coordinates)
            velocities.append(speed)
        for i in range(len(positions)):
            a1 = np.array([int(positions[i][0]), int(positions[i][1])])
            b1 = np.array([int(velocities[i][0]), int(velocities[i][1])])                
            for j in range(i+1, len(positions)):
                a2 = np.array([int(positions[j][0]), int(positions[j][1])])
                b2 = np.array([int(velocities[j][0]), int(velocities[j][1])])
                intersection = find_intersection(a1, b1, a2, b2)
                if intersection is not None:
                    if intersection[0] >= 200000000000000 and intersection[0] <= 400000000000000 and intersection[1] >= 200000000000000 and intersection[1] <= 400000000000000:
                        count = count + 1
                        print(count)
        print(count)

def find_intersection(a1, b1, a2, b2):
    # a1 and b1 define the first line: r1 = a1 + t * b1
    # a2 and b2 define the second line: r2 = a2 + s * b2

    # Check if lines are parallel
    det = b1[0] * b2[1] - b1[1] * b2[0]
    if det == 0:
        # Lines are parallel, no intersection
        return None
    # Solve for t and s
    t = np.linalg.det(np.array([a2 - a1, b2])) / det
    s = np.linalg.det(np.array([a2 - a1, b1])) / det
    if t <= 0 or s <= 0:
        return None

    # Calculate the intersection point
    intersection_point = a1 + t * b1

    return intersection_point


main()