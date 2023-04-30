#Name : Kseniia Katashova
# Доопрацюйте програму калькулятора, додайте операції цілочисельного поділу, поділу по модулю та зведення в ступінь


x = int (input("Enter x = "))
y =int( input("Enter y = "))

o = input ("Enter operation (+, -, * , //, %, **) ")

def add(x, y):
    return x + y

if o == "+":
    print("Result: ", add(x,y))
    
elif o == "-":
    print("Result: ", x - y)
elif o == "*":
    print("Result: ", x * y)
elif o == "/":
    print("Result: ", x / y)
elif o == "//":                 # Added new operation
    print("Result: ", x // y)   
elif o == "%":
    print("Result: ", x % y)    # Added new operation
elif o == "**":                 
    print("Result: ", x ** y)   # Added new operation
else:
    print("Invalid operator")
    
    

