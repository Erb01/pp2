#task1
import math
def degree_to_radian(degree):
    return degree*(math.pi/180)
degree = 15
radian = degree_to_radian(degree)
print(f"{radian:.6f}")

#task2
def area(height, base1, base2):
    return (1/2)*(base1+base2)*height
height = 5
base1 = 5
base2 = 6
area = area(height, base1, base2)
print(f"{area}")

#task3
import math
def regular_polygon_area(n, side_length):
    return (n*side_length**2)/(4*math.tan(math.pi/n))
n = 4  
side_length = 25
area = regular_polygon_area(n, side_length)
print(f"{round(area)}")

#task4
def parallelogram_area(base, height):
    return float(base*height)
base = 5
height = 6
area = parallelogram_area(base, height)
print(f"{area}")
