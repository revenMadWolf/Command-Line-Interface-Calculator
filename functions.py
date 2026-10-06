def multiplication(num1, num2):
    return num1*num2


def division(num1,num2):
    return num1/num2

def addition(num1,num2):
    return num1+num2

def subtraction(num1,num2):
    return num1-num2

def area_rectangle(length,width):
    return length*width

def area_circle(radius):
    return 3.142*radius**2

def area_triangle(base,height):
    return 1/2*base*height

def volume_cube(side):
    return side**3

def geometric_sequence(first_term,ratio,n):
    return first_term*ratio**(n-1)

def velocity(distance,time):
    return distance/time

def volume_cylinder(radius,height):
    return 3.142*radius**2*height

def airthmetic_sequence(first_term,difference,n):
    a,d=first_term,difference   #assigning into two variables to sort it 
    nth_term=a+(n-1)*d
    return nth_term