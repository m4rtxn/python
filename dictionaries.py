# mutable, unordered collection of items, each item in a dictionary is a key value pair where each key is unique in the dictionary

weekconversions = {
    "Sun" : "Sunday",
    "Mon":"Monday",
    "Tue":"Tuesday",
    "Wed" : "Wednesday",
    "Thu" : "Thursday",
    "Fry":"Friday",
    "Sat":"Saturday"
}

print(weekconversions["Wed"])

#Mostrar un mensaje en caso de error

print(weekconversions.get("Xfr","Not Found"))