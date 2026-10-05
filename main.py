import functions

<<<<<<< HEAD
def show_tasks(task_list):
    for task_id, task, assignee, status in task_list:
        print(f"{task_id}: {task} — Assigned to {assignee} ({status})")

show_tasks(tasks)
=======
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
    print("Answer:",answer)                #Output the answer



if int(selection) == 1:
    run_multiplication()
else:
    pass
>>>>>>> 6571236a7adc3fba7592a15fd5756a2c46917eeb
