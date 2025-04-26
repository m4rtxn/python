for word in "Medical":
    print(word)

for i in "Orange":
    print(i)

print("======================")

company = ["Apple","Microsoft","Epic Games","Samsung"]

for index in company:
    print(index)
print("======================")

for number in range(4,11):
    print(number)
print("======================")


#esto es lo mismo que el primer for
len(company)

for index in range(len(company)):
    print(company[index])
print("======================")
for n in range (10):
    if n == 0:
        print("Number 0")
    else:
        print("Other number")