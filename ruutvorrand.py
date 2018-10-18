from math import sqrt

#Just for clarification
#ax² + bx + c = 0
#a = ax²
#b = bx
#c = c

def quadratic_equation(a:int, b:int, c:int):
    try:
        #Full quadratic equation x = (-b +- sqrt(b² - 4ac)) / 2a

        #4ac calculation part from equation
        calculated_4ac = 4 * a * c

        #Full calculation under square root from equation
        calculated_sqrt = sqrt(b**2 - calculated_4ac)

        #Two final answers from quadratic equation
        x1 = (-b + calculated_sqrt) / (2 * a)
        x2 = (-b - calculated_sqrt) / (2 * a)

    except NameError:
        print("Error occurred!")
        print("Name error!")

    except ValueError:
        print("Error occurred!")
        print("Value error!")
        
    else:
        return x1, x2
    

# 7x² + 11x - 35 = 0
x1, x2 = quadratic_equation(7, 11, -35)
print(x1, x2)