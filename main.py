def operation(a, b, calculation):

    if calculation not in "+-*/":
        return "Please choose one of the + - * / operations."

    if calculation == "+":
        return(str(a) + " + " + str(b) + " = " + str(a+b))
    if calculation == "-":
        return(str(a) + " - " + str(b) + " = " + str(a-b))
    if calculation == "*":
        return(str(a) + " * " + str(b) + " = " + str(a*b))
    if calculation == "/":
        return(str(a) + " / " + str(b) + " = " + str(a/b))

while True:

    try:

        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        calculation = input("Choose your operation + - * / : ")

        print(operation(a, b, calculation))

    except:

        print("Please enter numbers correctly.")


