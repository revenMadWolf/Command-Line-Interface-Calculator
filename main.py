import functions


function_dict = {1:{"NAME":"Addition","FUNCTION":"run_addition()"},
                 2:{"NAME":"Subtraction","FUNCTION":"run_subtraction()"},
                 3:{"NAME":"Multiplication","FUNCTION":"run_multiplication()"},
                 4:{"NAME":"Division","FUNCTION":"run_division()"},
                 5:{"NAME":"Modulus","FUNCTION":"run_modulus()"},
                 6:{"NAME":"Area Of Triangle","FUNCTION":"run_area_triangle()"},
                 7:{"NAME":"Geometric Sequence","FUNCTION":"run_geometric_sequence()"},
                 8:{"NAME":"Cube volume","FUNCTION":"run_volume_cube()"},
                 9:{"NAME":"Circle area","FUNCTION":"run_area_circle()"}
                 10:{"NAME":"Cylinder Volume","FUNCTION":"run_volume_cylinder()"}
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


#Selcted subtraction
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
    print("selected Sqaure Area Calculator \n")
    length= int(input("Enter length: "))
    answer=functions.area_square(length)   #return the answer
    print(answer)

#trainagle's area selected
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
    
#Geomatric Sequence selected
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

#main loop of the program
while still_running:

    print("SELECT OPTION: ")

    for inner_set in function_dict.items():         #show the available functions
        print(inner_set[0],inner_set[1]["NAME"])

    selection = int(input("Enter Number: "))        #get the selected function index

    eval(function_dict[selection]["FUNCTION"])      #Run the function using eval() to convert string function to code

    still_running = input("Continue? (y/n)") == "y" #Ask the user if they want to continue using the calculator
