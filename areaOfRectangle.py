# Python Program to find Area of a Rectangle using Functions

def Area_of_a_Rectangle(width, height):

    # calculate the area
    Area = width * height

    # calculate the Perimeter
    Perimeter = 2 * (width + height)

    print("\n Area of a Rectangle is: %.2f" %Area)
    print(" Perimeter of Rectangle is: %.2f" %Perimeter)

Area_of_a_Rectangle(6, 4)