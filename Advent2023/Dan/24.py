'''
Go through every combination
Solve each combination and find if the solution is within the bound
This is Lamb's solution as I really like how it works
I like:
- Calling the main function and separating out the findintersection function
- I initially used a library to work out the unique combinations but taking the factorial with two 'for loops' is cleaner
- It gives lots of outs which return None to save time
- Neat use of linear algebra within numpy. I used GPT to make a nice diagram of what's happening 
  when we calculate the determinant of the two vectors of the velocities of two hailstones.
- Check out the appendix!
'''

import numpy as np
def main():
    with open("24.txt") as file:
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
            # This takes the x and y coordinates and their corresponding velocities
            a1 = np.array([int(positions[i][0]), int(positions[i][1])])
            b1 = np.array([int(velocities[i][0]), int(velocities[i][1])])     
            # This calculates the intersection for the coordinates and velocities of this particular loop 
            # with the remaining paths of the hailstones left other from the total set of loops
            # Hence, the algorithm runs in factorial time
            for j in range(i+1, len(positions)):
                a2 = np.array([int(positions[j][0]), int(positions[j][1])])
                b2 = np.array([int(velocities[j][0]), int(velocities[j][1])])
                intersection = find_intersection(a1, b1, a2, b2)
                if intersection is not None:
                    if intersection[0] >= 200000000000000 and intersection[0] <= 400000000000000 and intersection[1] >= 200000000000000 and intersection[1] <= 400000000000000:
                        count =+ 1
        print(count)

def find_intersection(a1, b1, a2, b2):
    # a1 and b1 define the first line: r1 = a1 + t * b1
    # a2 and b2 define the second line: r2 = a2 + s * b2
    # so we have two unknowns and two restrictions so there is a real solution
    # We can note that t and s represent time. So we have:
    # <0 is the past  
    # 0 is the present position of the hailstone
    # >0 is the future position of the hailstone. This is what we're interested in

    det = b1[0] * b2[1] - b1[1] * b2[0]
    # This checks if the lines are parallel, no intersection. See diagram at top
    if det == 0:
        return None
    # Solve for t and s using Cramer's rule. We have r1=r2 rearranged in Ax=b form where b is the difference of the intial positions
    # and Ax is the matrix of the coefficients. Hence we rearrange and replace a column in A with b. I put the explaination for how s is rearranged
    # for in the appendix as I orginally thought the columns of the matrix must be the other way round.

    t = np.linalg.det(np.array([a2 - a1, b2])) / det
    s = np.linalg.det(np.array([a2 - a1, b1])) / det
    if t <= 0 or s <= 0:
        return None

    # Calculate the intersection point using our solution for t and the first hailstone vector out of the two. 
    # It returns a list with two elements  
    intersection_point = a1 + t * b1
    print(intersection_point)

    return intersection_point


main()


'''
Appendix: 

# Consider a matrix formed by two vectors b1 and b2:
# | b1[0]  b2[0] |
# | b1[1]  b2[1] |
#
# The determinant of this matrix is calculated as:
# det = b1[0]*b2[1] - b1[1]*b2[0]
#
# Visually, it represents the area (in 2D) of the parallelogram formed by b1 and b2.
# If b1 and b2 are linearly independent (not parallel), this area is non-zero, and the determinant is non-zero.
# If b1 and b2 are linearly dependent (parallel), they form a degenerate parallelogram (line), so the area is zero, and hence the determinant is zero.
#
# The determinant can be visualized as:
#    |\
#    | \
#    |  \
#    |   \
# b1 |    \
#    |     \
#    |      \
#    |_______\
#       b2
#
# The area of this parallelogram is the absolute value of the determinant.
# It tells us if b1 and b2 are pointing in generally the same direction (small det) or perpendicular (large det).

# Cramer's Rule - Solving Linear Equations
# ----------------------------------------
# Cramer's Rule is a method to solve a system of linear equations using determinants.
# It is particularly useful when the system has the same number of equations as unknowns.

# Consider a system of 2 linear equations:
# a11*x + a12*y = b1
# a21*x + a22*y = b2

# This can be represented in matrix form as AX = B, where:
# A = | a11  a12 |       X = | x |       B = | b1 |
#     | a21  a22 |           | y |           | b2 |

# Cramer's Rule states that if det(A) is non-zero, the system has a unique solution.
# The solution can be found by replacing each column of A with B and calculating the determinant,
# then dividing by det(A).

# For our 2x2 system:
# det(A)  = a11*a22 - a12*a21
# det(Ax) = | b1  a12 | = b1*a22 - a12*b2
#           | b2  a22 |
# det(Ay) = | a11  b1 | = a11*b2 - b1*a21
#           | a21  b2 |

# Solutions:
# x = det(Ax) / det(A)
# y = det(Ay) / det(A)

# Visual Interpretation:
# - The determinant represents the area (in 2D) of the parallelogram formed by column vectors.
# - For Ax and Ay, we replace one of A's columns with B, altering the parallelogram.
# - The ratio of these areas (det(Ax)/det(A), det(Ay)/det(A)) gives the solution.
# - If det(A) is zero, the vectors are linearly dependent (parallel), and there's no unique solution.

# Note:
# Cramer's Rule is elegant but not efficient for large systems. 
# For computational purposes, methods like Gaussian elimination are generally preferred. It runs in O(n!) compared to quicker O(n^3) algos

# Applying Cramer's Rule to Find Intersection of Two Lines
# ---------------------------------------------------------
# The code snippet applies Cramer's Rule to solve for the intersection point 
# of two lines defined by parametric equations:
# Line 1: r1 = a1 + t*b1
# Line 2: r2 = a2 + s*b2
# where a1, a2 are initial points, and b1, b2 are direction vectors of the lines.

# Cramer's Rule Implementation:
# - To find the intersection, set r1 = r2 and solve for t and s, giving a system 
#   of linear equations.
# - This system can be expressed in matrix form. Cramer's Rule is used here to 
#   solve for t and s by calculating the determinant of matrices.

# Why Use the Difference of Initial Positions (a2 - a1):
# - The difference (a2 - a1) represents the vector connecting the initial points 
#   of the two lines. It is essential in forming the equations for the system.
# - By setting r1 = r2, we get a1 + t*b1 = a2 + s*b2. Rearranging gives
#   t*b1 - s*b2 = a2 - a1.
# - In Cramer's Rule context, (a2 - a1) becomes part of the constants vector 
#   in the linear system.

# Code Explanation:
# 1. For t:
#    - np.array([a2 - a1, b2]) forms a matrix by replacing the column for t 
#      in the coefficient matrix with (a2 - a1).
#    - np.linalg.det calculates its determinant. Dividing by 'det' (the determinant 
#      of the original coefficient matrix) gives the value of t.
# 2. For s:
#    - Similarly, np.array([a2 - a1, b1]) replaces the column for s, and its 
#      determinant is calculated and divided by 'det'.

# Summary:
# - The use of (a2 - a1) in the matrices results from rearranging the parametric 
#   line equations into a standard linear system. This difference represents the 
#   relative position of the lines, crucial for finding their intersection point.

# Rearranging Equations to Apply Cramer's Rule for Line Intersection
# -------------------------------------------------------------------
# Original Parametric Equations for two lines:
# Line 1: r1 = a1 + t*b1
# Line 2: r2 = a2 + s*b2
# Here, a1 and a2 are initial points, b1 and b2 are direction vectors.

# To find the intersection, set r1 equal to r2:
# a1 + t*b1 = a2 + s*b2
# Rearranging gives:
# t*b1 - s*b2 = a2 - a1

# Break this into component equations (assuming 2D for simplicity):
# t * b1_x - s * b2_x = a2_x - a1_x
# t * b1_y - s * b2_y = a2_y - a1_y

# Rearrange for Cramer's Rule:
# We need to isolate s in each equation. Rearrange as follows:
# -t * b1_x + s * b2_x = a1_x - a2_x
# -t * b1_y + s * b2_y = a1_y - a2_y

# Now, these are in the form A*x = B, where:
# A = matrix with columns [-b1_x, b2_x] and [-b1_y, b2_y]
# B = vector with components [a1_x - a2_x] and [a1_y - a2_y]

# Applying Cramer's Rule to solve for s:
# Replace the column associated with s in A with B, then compute the determinant.

# Determinant of original matrix A (det(A)):
# det(A) = (-b1_x * b2_y) - (-b1_y * b2_x)

# Matrix for solving s (A_s):
# A_s = matrix with columns [-b1_x, a1_x - a2_x] and [-b1_y, a1_y - a2_y]

# Determinant of A_s (det(A_s)):
# det(A_s) = (-b1_x * (a1_y - a2_y)) - (-b1_y * (a1_x - a2_x))

# Solve for s:
# s = det(A_s) / det(A)

# Note: This approach adapts Cramer's Rule to the structure of parametric line equations.
# It's necessary to rearrange the original equation to fit the form required for Cramer's Rule.


'''



