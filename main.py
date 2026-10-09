import functions
import os
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
RESET = "\033[0m"

categories = {
    1: {"NAME": "Basic Operations", "OPTIONS": [1, 2, 3, 4, 5,0]},
    2: {"NAME": "Area", "OPTIONS": [6, 7, 8, 9,0]},
    3: {"NAME": "Volume", "OPTIONS": [10,11,12, 13,0]},
    4: {"NAME": "Sequences", "OPTIONS": [14, 15,0]},
    5: {"NAME": "Physics", "OPTIONS": [16,0]},
    0: {"NAME": "Exit"}
}
category_colors = {
    1: GREEN,    # Basic Operations
    2: YELLOW,   # Area
    3: MAGENTA,  # Volume
    4: CYAN,     # Sequences
    5: RED,      # Physics
    0: RESET     # Exit
}

for number, category in categories.items():
    color = category_colors.get(number, RESET)
    print(f"{color}[{number}] {category['NAME']}{RESET}")

function_dict = {1:{"NAME":"Addition","FUNCTION":"run_addition()"},
                 2:{"NAME":"Subtraction","FUNCTION":"run_subtraction()"},
                 3:{"NAME":"Multiplication","FUNCTION":"run_multiplication()"},
                 4:{"NAME":"Division","FUNCTION":"run_division()"},
                 5:{"NAME":"Modulus","FUNCTION":"run_modulus()"},

                 6:{"NAME":"Area Of Triangle","FUNCTION":"run_area_triangle()"},
                 7:{"NAME":"Area of Circle","FUNCTION":"run_area_circle()"},
                 8:{"NAME":"Area of Square","FUNCTION":"run_area_square()"},
                 9:{"NAME":"Are of Rectangle","FUNCTION":"run_area_rectangle()"},
                 
                 10:{"NAME":"Cube volume","FUNCTION":"run_volume_cube()"},
                 11:{"NAME":"Cuboid volume","FUNCTION":"run_volume_cuboid()"},
                 12:{"NAME":"Sphere volume","FUNCTION":"run_volume_sphere()"},                             
                 13:{"NAME":"Cylinder Volume","FUNCTION":"run_volume_cylinder()"},

                 14:{"NAME":"Geometric Sequence","FUNCTION":"run_geometric_sequence()"},
                 15:{"NAME":"Arithmetic Sequence","FUNCTION":"run_arithmetic_sequence()"},

                 16:{"NAME":"Velocity","FUNCTION":"run_velocity()"},
                 0:{"NAME":"Back To Categories"}
                 }

#Function_dict structure: {selection_number:{"NAME":"The function name to display","FUNCTION":"Function to run"}
#save it like this so selection number and the function is connected.

#made to verify if the entered input does not break the program and asks the user to enter input till it gets a valid input
def validate_user_input(user_input, allowed_nums=None):
    try:
        user_input = float(user_input)
        if allowed_nums:
            if user_input in allowed_nums:
                return user_input
            else:
                print("No Option Found!")
                return validate_user_input(input("Choose again: "),allowed_nums)
        else:
            return user_input

    except ValueError:

        print("Invalid Input!")
        return validate_user_input(input("Enter Number: "),allowed_nums)


def get_input():
    input_list = []
    while True:  # Keep asking for new numbers to subtract
        num = input("Enter Number: ")  # Get the next number to subtraction answer
        if num:  # Stop asking for more numbers and leave the calculation
            input_list.append(validate_user_input(num))
        else:
            break
    return input_list

#Selected Multiplication
def run_multiplication():
    print("Selected Multiplication \n")
    inputs = get_input()
    answer = 1
    for num in inputs:
        answer = functions.multiplication(answer,num)
    print("Answer:",answer)
    #Output the answer

#Selcted Division
def run_division():
    print("Selected Division \n")

    answer = validate_user_input(input("Enter Number: "))

    inputs = get_input()
    for num in inputs:
        answer = functions.division(answer,num)
    print("Answer:",answer)
    #Output the answer
    
#Selected Addition
def run_addition():
    print("Selected Addition \n")
    inputs = get_input()
    answer = 0
    for num in inputs:
        answer = functions.addition(answer,num)
    print("Answer:",answer)
    #Output the answer


#Selected subtraction
def run_subtraction():
    print("Selected Subtraction \n")
    answer = validate_user_input(input("Enter Number: "))
    inputs = get_input()
    for num in inputs:
        answer = functions.subtraction(answer,num)
    print("Answer:",answer)
    #Output the answer


#Modulus selected 
def run_modulus():

    print("Selected Modulus \n")

    answer = validate_user_input(input("Enter First Number: "))
    num = validate_user_input(input("Enter Second Number: "))

    answer = functions.modulus(answer, num)

    print("Answer:", answer)
    

# rectangle's area selected
def run_area_rectangle():
    print("selected Rectangle Area Calculator \n")
    length= validate_user_input(input("Enter length: "))
    width= validate_user_input(input("Enter width: "))
    answer=functions.area_rectangle(length,width)   #return the answer
    print(answer)

#square's Area
def run_area_square():
    print("selected Square Area Calculator \n")
    length= validate_user_input(input("Enter length: "))
    answer=functions.area_square(length)   #return the answer
    print(answer)

#triangle's area selected
def run_area_triangle():
    print("Selected Triangle Area Calculator \n")
    base=validate_user_input(input("Enter base: "))
    height=validate_user_input(input("Enter height: "))
    answer=functions.area_triangle(base,height)
    print(answer)

#circle's Area
def run_area_circle():
    print("Selected Circle Area Calculator \n")
    radius=validate_user_input(input("Enter radius: "))
    answer= functions.area_circle(radius)
    print(answer)

#Volume of cube
def run_volume_cube():
    print("Selected volume of cube")
    length=validate_user_input(input("Enter length: "))
    answer=functions.volume_cube(length)
    print(answer)

#volume of cuboid
def run_volume_cuboid():
    print("Selected volume of cuboid")
    length=validate_user_input(input("Enter length: "))
    width=validate_user_input(input("Enter width: "))
    height=validate_user_input(input("Enter height: "))
    answer=functions.volume_cuboid(length, width, height)
    print(answer)

#volume of sphere
def run_volume_sphere():
    print("Selected volume of sphere")
    radius=validate_user_input(input("Enter radius: "))
    answer=functions.volume_sphere(radius)
    print(answer)

#cylinder's volume calculator selected
def run_volume_cylinder():
    print("Selected volume of cylinder")
    radius=validate_user_input(input("Enter radius: "))
    height=validate_user_input(input("Enter height: "))
    answer=functions.volume_cylinder(radius, height)
    print(answer)


#Geometric Sequence selected
def run_geometric_sequence():
    print("Selected Geometric Sequence Calculator \n")   #message that displays
    sequence = input("Enter sequence with commas: ")     # Ask the user to enter the starting terms, separated by commas 
    n = int(input("Enter required elements amount: "))
    numbers = sequence.split(",")                   # Split the input into strings, then convert each string to a number
    numbers = [float(num) for num in numbers]

# Calculate the common ratio from the first two terms
    common_ratio = numbers[1]/numbers[0]
    first_num = numbers[0]

    # Add terms until the sequence contains the requested number of elements
    while len(numbers) < n:
        numbers.append(functions.geometric_sequence(first_num,common_ratio,len(numbers)+1))

    print(numbers)

#Arithmetic sequence is selected
def run_arithmetic_sequence():
    print("Selected Arithmetic Sequence Calculator \n")
    sequence = input("Enter sequence with commas: ")
    n = int(input("Enter required elements amount: "))
    numbers = sequence.split(",")
    numbers = [float(num) for num in numbers]

    # Calculate the common difference
    common_difference = numbers[1] - numbers[0]
    first_num = numbers[0]

    # Add terms until the sequence contains the requested number of elements
    while len(numbers) < n:
        numbers.append(functions.arithmetic_sequence(first_num, common_difference, len(numbers)+1))

    print(numbers)

#selected Velocity
def run_velocity():
    print("Selected Velocity \n")
    distance = validate_user_input(input("Enter distance: "))
    time = validate_user_input(input("Enter time: "))
    answer = functions.velocity(distance, time)  # pass both arguments
    print("Answer:", answer)

#main loop of the program

still_running = True
os.system("cls")
while still_running:
    print(f"\n{CYAN}╭──────────────────────────────╮")
    print("│       ✦ CALCULATOR ✦         │")
    print(f"╰──────────────────────────────╯{RESET}")
    

    for number, category in categories.items():
        color = category_colors[number]
        print(f"{color}[{number}] {category['NAME']}{RESET}")

    category_choice = validate_user_input(input(f"\n{CYAN}Choose a category: {RESET}"),categories)
    if category_choice == 0:
        os.system("cls")
        break

    os.system("cls")
    selected_category = categories[category_choice]
    selected_color = category_colors[category_choice]

    while True:
        print(f"\n{selected_color}--- {selected_category['NAME']} ---{RESET}")

        for option_number in selected_category["OPTIONS"]:
            option_name = function_dict[option_number]["NAME"]
            print(f"{selected_color}[{option_number}] {option_name}{RESET}")

        option_choice = validate_user_input(input("Choose a calculation: "), selected_category["OPTIONS"])

        if option_choice == 0:
            os.system("cls")
            break

        eval(function_dict[option_choice]["FUNCTION"])
        continue_choice = input(
            f"\n{YELLOW}Do you want to continue? (y/n): {RESET}").lower()
        still_running = input("Continue? (y/n)") == "y" #Ask the user if they want to continue using the calculator
        if still_running == "y":
            os.system("cls")
        else:
            break
