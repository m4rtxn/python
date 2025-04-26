op = (input("Enter your operation"))
n1 = float(input("Enter your first number"))
n2 = float(input("Enter your second number"))



def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2


if op == "+":
    print(add(n1,n2))
elif op == "-":
    print(substract(n1,n2))
elif op =="*":
    print(multiply(n1,n2))
elif op =="/":
    print(divide(n1,n2))
else:
    print("Operation not valid")
