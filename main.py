import functions


function_dict = {1:"multiplication",2:"division"}

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

def run_area_rectangle():
    print("selected area_rectangle \n")
    length= int(input("Enter length: "))
    width=int(input("Enter width: "))
    answer=functions.area_rectangle(length,width)
    print(answer)


if int(selection) == 1:
    run_multiplication()
elif int(selection) == 2:
    run_division()
else:
    pass
    
    

