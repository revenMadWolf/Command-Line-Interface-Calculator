import functions


function_dict = {1:"addition",2:"subtraction",3:"multiplication",4:"division"}

print("SELECT OPTION: ")

for record in function_dict.items():
    print(record[0],record[1])

selection = int(input("Enter Number: "))


#Selected Multiplication
def run_multiplication():
    print("Selected Multiplication \n")
    answer = int(input("Enter Number: "))  #Initialize the answer
    while True:                            #Keep asking for new numbers to multiply by
        num = input("Enter Number: ")       #Get the next number to multiply answer by
        if num:                             #Stop asking for more numbers and leave the calculation
            answer = functions.multiplication(answer,int(num))
        else:
            break
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

if int(selection) == 1:
    run_addition()
elif int(selection) == 2:
    run_subtraction()
elif int(selection) == 3:
    run_multiplication
elif int(selection) == 4:
    run_division
else:
    pass
    
    

