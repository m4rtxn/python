def maxNumber(n1,n2,n3):
    if(n1>=n2 and n1>=n3):
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
       return n3

print(maxNumber(8,60,7))


age = 11
name = "Juan"

if age==18:
    print("You reached 18")
if age<18:
    print("You are a minor")
else:
    print("you are an adult")


print ("=============================")
if age <13:
    print("you are a child")
elif age>=13 and age<=17:
    print("you are a teenager")
else:
    print("you are an adult")