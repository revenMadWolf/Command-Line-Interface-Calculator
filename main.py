import functions


function_dict = {1:{"NAME":"Addition","FUNCTION":"run_addition()"},
                 2:{"NAME":"Subtraction","FUNCTION":"run_subtraction()"},
                 3:{"NAME":"Multiplication","FUNCTION":"run_multiplication()"},
                 4:{"NAME":"Division","FUNCTION":"run_division()"}
                 }

#Function_dict structure: {selection_number:{"NAME":"The function name to display","FUNCTION":"Function to run"}
#save it like this so selection number and the function is connected.

print("SELECT OPTION: ")

for record in function_dict.items():
    print(record[0],record[1])
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
    answer = int(input("Enter Number: "))  #Initialize the answer
    while True:                            #Keep asking for new numbers to divided by
        num = input("Enter Number: ")       #Get the next number to divide answer by
        if num:                             #Stop asking for more numbers and leave the calculation
            answer = functions.division(answer,int(num))
        else:
            break
    print("Answer:",answer) 
    
#Selected Addition
def run_addition():
    print("Selected Addition \n")
    answer = int(input("Enter Number: "))  #Initialize the answer
    while True:                            #Keep asking for new numbers to add
        num = input("Enter Number: ")       #Get the next number to add answer
        if num:                             #Stop asking for more numbers and leave the calculation
            answer = functions.addition(answer,int(num))
        else:
            break
    print("Answer:",answer)
#Selcted subtraction
def run_subtraction():
    print("Selected subtraction \n")
    answer = int(input("Enter Number: "))  #Initialize the answer
    while True:                            #Keep asking for new numbers to subtract
        num = input("Enter Number: ")       #Get the next number to subtraction answer
        if num:                             #Stop asking for more numbers and leave the calculation
            answer = functions.subtraction(answer,int(num))
        else:
            break
    print("Answer:",answer)


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



    
    
