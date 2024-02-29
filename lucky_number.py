#1/25/24
#group project making lucky numbers

name = input("Please Enter your Name")
month = int (input("Please Enter your Birth Month"))
day = int (input("Please Enter your Birthday"))
year = int (input("Please Enter your Birth year"))
nameLength = len(name)


a = nameLength + year
b = day + month

luckyNumber = a + b
print(name)
print(type(name))