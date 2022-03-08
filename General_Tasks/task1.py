# get the operation type firstly
operation_type = input("Operation Type: ")

# addition function
def add():

    fn = int(input("Enter First Number: "))
    sn = int(input("Enter Second Number: "))

    print(f"Result is {fn + sn}")

# subtraction function
def subtract():

    fn = int(input("Enter First Number: "))
    sn = int(input("Enter Second Number: "))

    print(f"Result is {fn - sn}")

# multiplication function
def multiply():

    fn = int(input("Enter First Number: "))
    sn = int(input("Enter Second Number: "))

    print(f"Result is {fn * sn}")

# division function
def divide():

    fn = int(input("Enter First Number: "))
    sn = int(input("Enter Second Number: "))

    print(f"Result is {fn / sn}")

# square root function
def sqrt():

    n = int(input("Enter Number: "))

    print(f"Result is {n ** 0.5}")

# square root function
def power():

    b = int(input("Enter Basis: "))
    e = int(input("Enter Exponent: "))

    print(f"Result is {b ** e}")

# fraction function
def fraction():

    n = int(input("Enter Numerator: "))
    d = int(input("Enter Denomerator: "))

    print(f"Result is {n}/{d}")

# integration function
def integrate():

    b = input("Enter first-degree Equation: ")

    print(f"Result is {int(b[0])/2} {b[1]}^2 + c")



# condition for operation type

if operation_type == "+" or operation_type == "add":
    add()

elif operation_type == "-" or operation_type == "subtract":
    subtract()

elif operation_type == "*" or operation_type == "multiply":
    multiply()

elif operation_type == "/" or operation_type == "divide":
    divide()

elif operation_type == "√" or operation_type == "sqrt":
    sqrt()

elif operation_type == "**" or operation_type == "power":
    power()

elif operation_type == "o/o" or operation_type == "fraction":
    fraction()

elif operation_type == "∫" or operation_type == "integrate":
    integrate()