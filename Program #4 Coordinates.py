# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 

import math

def distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + 
                     (coord2[1] - coord1[1]) ** 2 + 
                     (coord2[2] - coord1[2]) ** 2)

def main():
    while True:
        try:
            x1, y1, z1 = map(float, input("Enter the first coordinate (x1, y1, z1) separated by spaces: ").split())
            x2, y2, z2 = map(float, input("Enter the second coordinate (x2, y2, z2) separated by spaces: ").split())
            coord1 = (x1, y1, z1)
            coord2 = (x2, y2, z2)
            break
        except ValueError:
            print("Invalid input. Please enter numeric values for coordinates.")

    dist = distance(coord1, coord2)
    print(f"The distance between the points {coord1} and {coord2} is: {dist:.2f}")

main()
