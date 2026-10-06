import functions


function_dict = {1:{"NAME":"Addition","FUNCTION":"run_addition()"},
                 2:{"NAME":"Subtraction","FUNCTION":"run_subtraction()"},
                 3:{"NAME":"Multiplication","FUNCTION":"run_multiplication()"},
                 4:{"NAME":"Division","FUNCTION":"run_division()"},
                 5:{"NAME":"Modulus","FUNCTION":"run_modulus()"},
                 6:{"NAME":"Area Of Triangle","FUNCTION":"run_area_rectangle()"}
                 
                 }

#Function_dict structure: {selection_number:{"NAME":"The function name to display","FUNCTION":"Function to run"}
#save it like this so selection number and the function is connected.

print("SELECT OPTION: ")

for inner_set in function_dict.items():
    print(inner_set[0],inner_set[1]["NAME"])

selection = int(input("Enter Number: "))

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

def run_modulus():
    print("Selected Modulus \n")
    answer=float(input("Enter number: "))
    inputs = get_input()
    for num in inputs:
        answer = functions.modulus(answer,num)
    print("Answer:",answer)
    #Output the answer
    


def run_area_rectangle():
    print("selected area_rectangle \n")
    length= int(input("Enter length: "))
    width=int(input("Enter width: "))
    answer=functions.area_rectangle(length,width)   #return the answer
    print(answer)

def run_area_triangle():
    print("Selected area_triangle \n")
    base=int(input("Enter base: "))
    height=int(input("Enter height: "))
    answer=functions.area_triangle(base,height)
    print(answer)



eval(function_dict[selection]["FUNCTION"])
