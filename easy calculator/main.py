from art import logo
print(logo)


#Add function
def add(n1, n2):
    return n1 + n2
#Subtract function
def subtract(n1, n2):
    return n1 - n2
#multiply function
def multiply(n1, n2):
    return n1 * n2
#divide function
def devide(n1, n2):
    return n1 / n2
#operations book
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : devide,
}
def calculation():
    
    #number1
    while True:
        try:
            n1 = float(input("What is first number?: "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break    
    #operations display
    for symbol in operations:
        print(symbol)
    #main function
    should_continue = True 
    while should_continue:
        #operation input
        while True:
            operation = input("Pick an operation: ")
            if operation not in operations:
                print("invalid operation")
                continue
            else:
                break
        #number2
        while True:
            try:
                n2 = float(input("What is next number?: "))
            except ValueError:
                print("Not an integer!")
                continue
            else:
                break   
        calculation_function = operations[operation]
        answer = calculation_function(n1, n2)  
        print(f"{n1} {operation} {n2} = {answer}")
        #Do you want to add a number?
        while True:
            __ask__ = input("Do you want to add number? yes'y' no'n'")
            if __ask__ == "y":
                n1 = answer 
                break
            elif __ask__ == "n":
                should_continue = False
                print(f"Your final answer is {answer}. Good bye!")
                break
            else:
                print("What?")
                continue
calculation()

