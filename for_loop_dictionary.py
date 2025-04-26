dictionary = {'name':'Juan','age':'23'}

print(dictionary.items())
print("=================")
for key, value in dictionary.items():
    print(key,":",value)

print("=================")
#solo keys
for key in dictionary.keys():
    print(key)
print("=================")
#solo valores
for value in dictionary.values():
    print(value)