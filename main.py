import functions
categories = {
    1: {"NAME": "Basic Operations", "OPTIONS": [1, 2, 3, 4, 5]},
    2: {"NAME": "Area", "OPTIONS": [6, 7, 8, 9]},
    3: {"NAME": "Volume", "OPTIONS": [10, 13]},
    4: {"NAME": "Sequences", "OPTIONS": [14, 15]},
    5: {"NAME": "Physics", "OPTIONS": [16]},
}


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
                 
                             
                 13:{"NAME":"Cylinder Volume","FUNCTION":"run_volume_cylinder()"},

                 14:{"NAME":"Geometric Sequence","FUNCTION":"run_geometric_sequence()"},
                 15:{"NAME":"Arithmetic Sequence","FUNCTION":"run_arithmetic_sequence()"},

                 16:{"NAME":"Velocity","FUNCTION":"run_velocity()"}
                 }

#Function_dict structure: {selection_number:{"NAME":"The function name to display","FUNCTION":"Function to run"}
#save it like this so selection number and the function is connected.






def get_input():
    input_list = []
    while True:  # Keep asking for new numbers to subtract
        num = input("Enter Number: ")  # Get the next number to subtraction answer
        if num:  # Stop asking for more numbers and leave the calculation
            input_list.append(int(num))
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
    answer=float(input("Enter number: "))
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
    answer=float(input("Enter number: "))
    inputs = get_input()
    for num in inputs:
        answer = functions.subtraction(answer,num)
    print("Answer:",answer)
    #Output the answer


#Modulus selected 
def run_modulus():

    print("Selected Modulus \n")

    answer = float(input("Enter first number: "))
    num = float(input("Enter second number: "))

    answer = functions.modulus(answer, num)

    print("Answer:", answer)
    

# rectangle's area selected
def run_area_rectangle():
    print("selected Rectangle Area Calculator \n")
    length= int(input("Enter length: "))
    width=int(input("Enter width: "))
    answer=functions.area_rectangle(length,width)   #return the answer
    print(answer)

#square's Area
def run_area_square():
    print("selected Square Area Calculator \n")
    length= int(input("Enter length: "))
    answer=functions.area_square(length)   #return the answer
    print(answer)

#triangle's area selected
def run_area_triangle():
    print("Selected Triangle Area Calculator \n")
    base=int(input("Enter base: "))
    height=int(input("Enter height: "))
    answer=functions.area_triangle(base,height)
    print(answer)

#circle's Area
def run_area_circle():
    print("Selected Circle Area Calculator \n")
    radius=int(input("Enter radius: "))
    answer= functions.area_circle(radius)
    print(answer)

def run_volume_cube():
    print("Selected volume")
    length=float(input("Enter the length: "))
    answer=functions.volume_cube(length)
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

#cylinder's volume calculator selected
def run_volume_cylinder():
    print("Selected Cylinder Volume Calculator \n")
    radius=int(input("Enter Radius: "))
    height=int(input("Enter height: "))
    answer=functions.volume_cylinder(radius, height)
    print(answer)

still_running = True

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
    distance = float(input("Enter distance: "))
    time = float(input("Enter time: "))
    answer = functions.velocity(distance, time)  # pass both arguments
    print("Answer:", answer)

#main loop of the program

still_running = True

while still_running:
    print("\n=== CALCULATOR ===")
    for number, category in categories.items():
        print(number, category["NAME"])
    print("0 Exit")

    category_choice = input("Choose a category: ")

    if category_choice == "0":
        break

    if not category_choice.isdigit() or int(category_choice) not in categories:
        print("Please choose a category from the list.")
        continue

    selected_category = categories[int(category_choice)]

    while True:
        print(f"\n--- {selected_category['NAME']} ---")

        for option_number in selected_category["OPTIONS"]:
            print(option_number, function_dict[option_number]["NAME"])

        print("0 Back to categories")
        option_choice = input("Choose a calculation: ")

        if option_choice == "0":
            break

        if not option_choice.isdigit():
            print("Please enter a number.")
            continue

        option_choice = int(option_choice)

        if option_choice in selected_category["OPTIONS"]:
            eval(function_dict[option_choice]["FUNCTION"])
            still_running = input("Continue? (y/n)") == "y" #Ask the user if they want to continue using the calculator
            if still_running != "y":
                still_running = False
                break
