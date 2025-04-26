
years=[2000,2006,2007,1990]

company = ["Microsoft","Apple","Samsung","Tencent"]

company[1]="Apol"
print(company[0:len(company)])
company.extend(years)

print("concatenando ambos arreglos")
print(company)


company.append("Epic Games")
print(company)


company.remove(company[1])

print(company)

company.clear()

print(company)

print(years)
years.sort()
print(years)
years.reverse()
print(years)


newYears = years.copy()
print(newYears)
newYears.append(2012)
print(newYears)

