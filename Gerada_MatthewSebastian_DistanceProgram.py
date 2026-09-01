import math
import time


# Failsafe so the program doesn't crash when you input a string.
def get_values(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That is not a number.")


# Ask user for coordinates of first and second point.
print("Input values to get distance. Your values must be valid numbers.")
x1 = get_values("Define x coordinate of point 1:")
x2 = get_values("Define x coordinate of point 2:")
y1 = get_values("Define y coordinate of point 1:")
y2 = get_values("Define y coordinate of point 2:")

# Compute the distance between the two points.
d = math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

# Print out distance.
print("The distance is", d)

time.sleep(4)
exit()
