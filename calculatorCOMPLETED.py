# Advanced Calculator Application

import math
import statistics

## Error checking functions##

# Get a valid number in lowerRange-upperRange
def get_valid_num_in_range(prompt, lowerRange, upperRange, errorMessage):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < lowerRange or value > upperRange:
            print(errorMessage)
            continue
        else:
            break
    return value

# Gets the user to choose between two defined options
def get_valid_two_option_string(prompt, option1, option2, errorMessage):
    while True:

        value = input(prompt)

        if value != option1 and value != option2:
            print(errorMessage)
        else: 
            break

    return value

# Get a valid float (decimal number)
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            break
        except ValueError:
            print("Sorry, I didn't understand that. Please input an integer or decimal number")

    return value

# Get a valid non negative float
def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Sorry, your response must be a non negative integer or decimal number.")
            continue

        if value < 0:
            print("Sorry, your response must be a non negative integer or decimal number.")
            continue
        else:
            break
    return value

# Get a non negative integer function
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value

## Selection menus for user ##
# Type of calculation options user can choose from
# Once user has selected one, they will be given additional 
# selection options with more specific calculation options related to their choice

calcOptions = [
    "Simple Calculations",
    "Geometry Calculations",
    "Linear Equation Calculations",
    "Advanced Mathematics",
]

simpleCalcOptions = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Square root of a number",
    "Raise a number to the exponent of another"
]

geometryCalcOptions = [
    "Calculate the area of a shape (Rectangle, square, triangle or circle)",
    "Calculate the perimeter of a shape (Rectangle, square, triangle or circle)",
    "Calculate the volume of a shape (Cube, cone or sphere)"
]

linearEquationCalcOptions = [
    "Calculate the slope",
    "Calculate the y-intercept given a point on the line and the slope",
    "Calculate the x-intercept",
    "Calculate the slope of the reciprocal"
]

advancedMathematicsCalcOptions = [
    "Calculate the mean of a list of numbers",
    "Calculate the mode of a list of numbers",
    "Calculate the median of a list of numbers"
]

shapeOptionsForPerAndArea = [
    "Rectangle",
    "Square",
    "Triangle",
    "Circle"
]

shapeOptionsForVolume = [
    "Cube",
    "Cone",
    "Sphere"
]

# Introduction welcomes user to the program and guides user into choosing which calculation they'd like to perform
def main():
    print("Welcome to Chloe's Calculator! Here you'll be able to chose from a variety of calculations ranging from simple to advanced.")
    print("Below is a list of the types of calculations you can make.")
    counter = 1
    for i in calcOptions:
        print("(" + str(counter) + ") " + i)
        counter += 1
    choice = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(calcOptions), "Please input a valid number (1-" + str(len(calcOptions)) + ")")
    
    # Depending on their choice, they will be given different more specific options
    if (choice == 1):
        # User chose simple calculations
        simpleChoicePhase()

    elif (choice == 2):
        # User chose geometry calculations
        geometryCalculations()

    elif (choice == 3):
        # User chose linear equation calculations
        linearEquationCalculations()

    elif (choice == 4): 
        # User chose advanced mathematics calculations
        advancedMathematicsCalculations()

# User chooses to be more specific about the type of calc they want to do 
# e.g : simple calculation --> addition
def simpleChoicePhase():
    print("Below are options to specify the calculation you want to make")
    counter = 1
    for i in simpleCalcOptions:
        print("(" + str(counter) + ") " + i)
        counter += 1
    choice = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(simpleCalcOptions), "Please input a valid number (1-" + str(len(simpleCalcOptions)) + ")")
    if (choice == 1):
        # User chose addition
        # User inputs the two numbers to be added together 
        x = get_valid_float("Input the first number you want to add: ")
        y = get_valid_float("Input the second number you want to add: ")
        sum = addition(x, y)
        print("The sum of the addition is: " + str(sum))
        # TODO print a message along with result 

    elif (choice == 2):
        # User chose subtraction
        # User inputs the two numbers to be subtracted together 
        x = get_valid_float("Input the first number you want to subtract: ")
        y = get_valid_float("Input the second number you want to subtract: ")
        difference = subtraction(x, y)
        print("The result of the subtraction is: " + str(difference))

    elif (choice == 3):
        # User chose multiplication
        # User inputs the two numbers to be multiplied together 
        x = get_valid_float("Input the first number you want to multiply: ")
        y = get_valid_float("Input the second number you want to multiply: ")
        product = multiplication(x, y)
        print("The result of the multiplication is: " + str(product))

    elif(choice == 4):
        # User chose division
        # User inputs the two numbers to be divided together 
        x = get_valid_float("Input the first number you want to divide: ")
        # This loop makes sure user cannot divide by zero 
        while True:
            y = get_valid_float("Input the second number you want to divide: ")
            if y == 0:
                print("Please input a value that is not zero. Division by zero is undefined.")
            else:
                break 

        quotient = division(x, y)
        print("The result of the division is: " + str(quotient))

    elif (choice == 5):
        # User chose square root
        # User inputs the the number they want to take the square root of 
        # This loop makes sure user cannot divide by zero 
        while True:
            x = get_valid_float("Input the number you want the square root of.: ")
            if x < 0:
                print("Please input a positive value. You cannot take the square root of a negative number.")
            else:
                break 
        
        sqrt = squareRoot(x)
        print("The square root is: " + str(sqrt))

    elif (choice == 6):
        # User chose exponent
        # User inputs the two numbers. The first on will be the base raised to the power of the second number
        x = get_valid_float("Input the base: ")
        y = get_valid_float("Input the exponent ")
        raisedNum = toThePowerof(x, y)
        print("The resulting number is: " + str(raisedNum))


def geometryCalculations():
    print("Below are options to specify the calculation you want to make")
    counter = 1
    for i in geometryCalcOptions:
        print("(" + str(counter) + ") " + i)
        counter += 1
    choice = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(geometryCalcOptions), "Please input a valid number (1-" + str(len(geometryCalcOptions)) + ")")
    
    if (choice == 1):
        # User chose area
        counter = 1
        for i in shapeOptionsForPerAndArea:
            print("(" + str(counter) + ") " + i)
            counter += 1
        shape = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(shapeOptionsForPerAndArea), "Please input a valid number (1-" + str(len(shapeOptionsForPerAndArea)) + ")")

        # Chooses which shape the user is calculating the area for 
        if (shape == 1):
            # User chose Rectangle
            length = get_non_negative_float("Input the length of the rectangle: ")
            width = get_non_negative_float("Input the width of the rectangle: ")
            area = rectangleArea(length, width)
            print("The area of the rectangle is: " + str(area))

        elif (shape == 2):
            # User chose square 
            sideLength = get_non_negative_float("Input the side length of the square: ")
            area = squareArea(sideLength)
            print("The area of the square is: " + str(area))
        
        elif (shape == 3): 
            # User chose triangle 
            base = get_non_negative_float("Input the length of the base of the triangle: ")
            height = get_non_negative_float("Input the height of the triangle: ")
            area = triangleArea(base, height)
            print("The area of the triangle is: " + str(area))

        elif (shape == 4):
            # User chose circle
            radius = get_non_negative_float("Input the length of the radius of the circle: ")
            area = circleArea(radius)
            print("The area of the circle is: " + str(area))
            
    
    elif (choice == 2):
        # User chose perimeter 
        counter = 1
        for i in shapeOptionsForPerAndArea:
            print("(" + str(counter) + ") " + i)
            counter += 1
        shape = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(shapeOptionsForPerAndArea), "Please input a valid number (1-" + str(len(shapeOptionsForPerAndArea)) + ")")

        # Chooses which shape the user is calculating the perimeter for 
        if (shape == 1):
            # User chose Rectangle
            length = get_non_negative_float("Input the length of the rectangle: ")
            width = get_non_negative_float("Input the width of the rectangle: ")
            perimeter = rectanglePerimeter(length, width)
            print("The perimeter of the rectangle is: " + str(perimeter))
            
        elif (shape == 2):
            # User chose square 
            sideLength = get_non_negative_float("Input the side length of the square: ")
            perimeter = squarePerimeter(sideLength)
            print("The perimeter of the square is: " + str(perimeter))
            
        
        elif (shape == 3): 
            # User chose triangle 
            sideLength1 = get_non_negative_float("Input the length of side 1: ")
            sideLength2 = get_non_negative_float("Input the length of side 2: ")
            sideLength3 = get_non_negative_float("Input the length of side 3: ")
            perimeter = trianglePerimeter(sideLength1, sideLength2, sideLength3)
            print("The perimeter of the triangle is: " + str(perimeter))
            

        elif (shape == 4):
            # User chose circle
            radius = get_non_negative_float("Input the length of the radius of the circle: ")
            perimeter = circlePerimeter(radius)
            print("The perimeter of the circle is: " + str(perimeter))
            

    elif (choice == 3):
        # User chose volume 
        counter = 1
        for i in shapeOptionsForVolume:
            print("(" + str(counter) + ") " + i)
            counter += 1
        shape = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(shapeOptionsForVolume), "Please input a valid number (1-" + str(len(shapeOptionsForVolume)) + ")")

        if (shape == 1):
            # User chose cube
            sideLength = get_non_negative_float("Input the length of the cube: ")
            volume = cubeVolume(sideLength)
            print("The volume of the cube is: " + str(volume))

        elif (shape == 2):
            # User chose cone 
            radiusOfBase = get_non_negative_float("Input the length of the radius of the base: ")
            height = get_non_negative_float("Input the height of the cone: ")
            volume = coneVolume(radiusOfBase, height)
            print("The volume of the cone is: " + str(volume))
        
        elif (shape == 3): 
            # User chose sphere 
            radius = get_non_negative_float("Input the radius of the sphere: ")
            volume = sphereVolume(radius)
            print("The volume of the sphere is: " + str(volume))




def linearEquationCalculations():
    print("Below are options to specify the calculation you want to make")
    counter = 1
    for i in linearEquationCalcOptions:
        print("(" + str(counter) + ") " + i)
        counter += 1
    choice = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(linearEquationCalcOptions), "Please input a valid number (1-" + str(len(linearEquationCalcOptions)) + ")")
    if (choice == 1):
        # User chose to calc slope
        # User inputs the coordinates of two points on the line
        # Point 1 coords
        x1 = get_valid_float("Input X1: ")
        y1 = get_valid_float("Input Y1: ")
        # Point 2 corrds
        x2 = get_valid_float("Input X2: ")
        y2 = get_valid_float("Input Y2: ")
        # Points are plugged into slope calculation function
        slope = slopeCalculation(x1, y1, x2, y2)
        print("The slope of this line is: " + str(slope))
        
    elif (choice == 2):
        # User chose to calc y-int
        # Gets a point on the line from the user 
        x = get_valid_float("Input X: ")
        y = get_valid_float("Input Y: ")
        # Gets the slope from the user
        slope = get_valid_float("Input slope: ")
        # Point and slope is plugged into y-int calc
        yint = yinterceptCalculation(x, y, slope)
        print("The y-intercept of this line is: " + str(yint))
        
    elif (choice == 3):
        # User chose to calc x-int
        # Gets a point on the line from the user 
        x = get_valid_float("Input X: ")
        y = get_valid_float("Input Y: ")
        # Gets the slope from the user
        slope = get_valid_float("Input slope: ")
        # y-int and slope are plugged into x-int calc
        xint = xinterceptCalculation(x, y, slope)
        print("The x-intercept of this line is: " + str(xint))

    elif (choice == 4):
        # Gets the slope from the user
        slope = get_valid_float("Input slope: ")
        # Point and slope is plugged into recipslope calc
        recipSlope = recipSlopeCalculation(slope)
        print("The reciprocal slope is: " + str(recipSlope))



def advancedMathematicsCalculations():
    print("Below are options to specify the calculation you want to make")
    counter = 1
    for i in advancedMathematicsCalcOptions:
        print("(" + str(counter) + ") " + i)
        counter += 1
    choice = get_valid_num_in_range("Please select the corresponding number from the above menu. ", 1, len(advancedMathematicsCalcOptions), "Please input a valid number (1-" + str(len(advancedMathematicsCalcOptions)) + ")")

    if (choice == 1):
        # User chose to calculate mean
        # User specifies the size of the array 
        arraySize = get_non_negative_int("Please input an integer to determine the size of the array: ")
        
        # Array is plugged into mean calculation where the mean is calculated then returned 
        mean = meanCalculation(arraySize)
        print("The mean is: " + str(mean))
            
    elif (choice == 2):
        # User chose to calculate mode
        # User specifies the size of the array 
        arraySize = get_non_negative_int("Please input an integer to determine the size of the array: ")

        # Array is plugged into mode calculation where the mode is calculated then returned 
        mode = modeCalculation(arraySize)

        if len(mode) == arraySize:
            finalMode = "No mode found"
        else:
            finalMode = "The mode(s) is/are " + ', '.join(map(str, mode))
        
        print(finalMode)


        
    elif (choice == 3):
        # User chose to calculate median
        # User specifies the size of the array 
        arraySize = get_non_negative_int("Please input an integer to determine the size of the array: ")
        # Array is plugged into mode calculation where the mode is calculated then returned 
        median = medianCalculation(arraySize)
        print("The median is: " + str(median))


# The below functions are the actual calculation functions

### Simple calculations ###

# Addition 
# Takes two numbers and returns their sum
def addition(x, y):
    # TODO user chooses how many numbers they want to add together
    sum = x + y
    return sum 

# Subtraction
# Takes two numbers and returns their difference 
def subtraction(x, y):
    # TODO user chooses how many numbers they want to subtract
    difference = x - y
    return difference

# Multiplication
# Takes two numbers and returns their product
def multiplication(x, y):
    # TODO user chooses how many numbers they want to multiply together
    product = x * y 
    return product

# Division 
# Takes two numbers and returns their quotient 
def division(x, y):
    # TODO user chooses how many numbers they want to divide
    quotient = x / y 
    return quotient

# Square root
# Returns the square root of x
def squareRoot(x):
    sqrtOfNum = math.sqrt(x)
    return sqrtOfNum

# Powers and exponents
# Returns x to the power of y  
def toThePowerof(x, y):
    z = math.pow(x, y)
    return z

### Geomentry Calculations ###
 
## Calculating the area of shapes ##

# Rectangle 
def rectangleArea (l, w):
    area = l * w
    return(area)

# Square
def squareArea (sideLength):
    area = math.pow(sideLength, 2)
    return(area)

# Triangle
def triangleArea(base, height):
    area = base * height / 2
    return(area)

# Trapezoid
# TODO check if this is needed
def trapezoidArea(a, b, h):
    area = ((a + b) / 2) * h
    return area 

# Circle
def circleArea(r):
    area = math.pi * math.pow(r, 2)
    return area

## Calculating the perimeter of shapes ##
# Rectangle
def rectanglePerimeter(l, w): 
    perimeter = 2 * l + 2 * w
    return perimeter 

# Square 
def squarePerimeter(l):
    perimeter = 4 * l
    return perimeter 

# Triangle
def trianglePerimeter(a, b, c): 
    perimeter = a + b + c
    return perimeter

# Trapezoid 
def trapezoidPerimeter(a, b, c, d): 
    perimeter = a + b + c + d
    return perimeter

# Circle
def circlePerimeter(radius): 
    perimeter = 2 * math.pi * radius
    return perimeter 

## Volume calculations ##
def cubeVolume(sideLength):
    volume = math.pow(sideLength, 3)
    return volume

def coneVolume(radiusOfBase, height):
    volume = math.pi * math.pow(radiusOfBase, 2) * height / 3
    return volume 

def sphereVolume(radius):
    volume = math.pi * math.pow(radius, 3) * 4 / 3
    return volume 

### Algebra Linear Equations: (y = ax + b) ###
# Calculating slope
def slopeCalculation (x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1) 
    return slope

# Calculate y-intercept given a point on the line and the slope
def yinterceptCalculation(x, y, slope):
    # y = mx +b
    # y = slope * x + b
    # y - slope * x = b
    b = y - slope * x
    return b 

# Calculate x intercept 
def xinterceptCalculation(x, y, slope):
    # y = mx + b
    # 0 = slope * x + b
    # -b = slope * x
    # -b/slope = x
    yint = yinterceptCalculation(x, y, slope)
    x = ((-yint) / slope)
    return x 

# Calculate the slope of the reciprocal 
def recipSlopeCalculation(slope):
    recipSlope = -1/slope
    return recipSlope

# Mean and mode 
# Using an array of numbers calculate the mean
def meanCalculation(arraySize):
    array = []
    sumOfArray = 0
    # User fills array with elements
    for i in range(arraySize):
        number = get_valid_float("Number to be inserted into array: ")
        sumOfArray += number
        array.append(number)
    mean = sumOfArray / arraySize
    return mean

# Using an array of numbers calculate the mode 
def modeCalculation(arraySize):
    array = []
    # TODO fix this

    # User fills array with elements
    for i in range(arraySize):
        number = get_valid_float("Number to be inserted into array: ")
        array.append(number)

    freqData = statistics.Counter(array)
    gettingMode = dict(freqData)
    mode = [k for k, v in gettingMode.items() if v == max(list(freqData.values()))]

    return mode


# Using an array of numbers calculate the median
def medianCalculation(arraySize):
    array = []

    # User fills array with elements
    for i in range(arraySize):
        number = get_valid_float("Number to be inserted into array: ")
        array.append(number)
    
    # Order the list
    array.sort()

    # Finding median (Two middle numbers)
    # If the array is of an even length 
    if (len(array) % 2 == 0):
        middleNum1 = array[len(array) // 2]
        middleNum2 = array[len(array) // 2 - 1]
        median = ((middleNum1 + middleNum2) / 2)
    # The array is of an odd length (One middle number)
    else:
        median = array[len(array) // 2]

    return median

# Global var
playAgainBool = True


def playMore():

    answer = get_valid_two_option_string("Would you like to make another calcuation?: (yes/no) ", "yes", "no", "Please enter \"yes\" or \"no\"")
    if (answer == "yes"):
        playAgainBool = True
    else: 
        playAgainBool = False
        goodbye()

def goodbye():
    print("Thank you for using Chloe's Calculator ™. Come calculate again!")
    exit()

def order():
    while playAgainBool == True:
        main()
        playMore()

# order function 
order()




