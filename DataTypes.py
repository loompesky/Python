# #To know the data types we use the type() function
# #assign a value either number or string to a variable
# x1 = 4
# type(x1)

# type(-2)
# #out: integer

# type(8.45)
# #output: float

# #you can change a number to an integer or a float by using the int() or the float()
# float(7)
# #output: 7.0

# x3 = 5.333
# int(x3)

# y = 10
# #print str(y) + " Dollars"

# #first_name = input("Enter your fist name: ")
# #last_name = input("Enter your second name: ")
# #print()
# #print("My name is " + first_name + ' ' + last_name)
# #to capitalize the names
# #print("My name is " + first_name.capitalize() + ' ' + last_name.capitalize())
# #to lower case the name and Capitalize the last name
# #print("My name is " + first_name.lower() + ' ' + last_name.capitalize())
# #to lower case the name and upper case the last name
# #print("My name is " + first_name.lower() + ' ' + last_name.upper())

# #formatting in python strings
# #output = "Yello, {} {}" .format(first_name,last_name)
# #output = "Yello, {0} {1}" .format(first_name,last_name)
# #Only available in Python 3
# #print(output)
# #output = f"Hello, {first_name} {last_name}"
# #print(output)

# #dealing with numbers
# # pi = 3.14159
# # print(pi)

# #see the values as  number
# # first_num = input("Enter the first number: ")
# # second_num = input("Enter the second number: ")
# # print(int(first_num) + int(second_num))
# # print(int(first_num) - int(second_num))
# # print(float(first_num) * float(second_num))
# # print(float(first_num) / float(second_num))
# # print(int(first_num) ** int(second_num))

# days_in_february = 28
# print(str(days_in_february) + ' ' + "is the total number of days in February")

# #see the values as a string
# #first_num = "10"
# #second_num = "5"
# #print(first_num + second_num)


#List,Arrays,Dictionary
#Dictionary
maame = {}
maame["first"] = "Agnes"
maame["last"] = "Pokua"

prince = {}
prince["first"] = "Prince"
prince["last"] = "Frimpong"

people = []
people.append(maame)
people.append(prince)
people.append({
    "first" : "Bill", "last" : "Gates"
})
print(people)