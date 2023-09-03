# # #print output to a console
# # print("This is Prince")
# # #getting information from the user
# # name = input("Please enter your name: ")
# # print(name)
# # #printing blank lines can improve readability
# # print("My name is Prince Frimpong")
# # print()
# # see = input("Did you see that blank line?:")
# # print(see)
# # #\n creates a new line
# # print("Blank line \nin the middle of string")

# # #using print as a dubugging tool
# # print("adding numbers")
# # x = 2 + 5
# # print(x)
# # print ("dividiing numbers") 
# # #y = x / 0
# # y = x / 2
# # print(y)

# print(3 + 5.0)

price = input("How much did you pay? ")
price = float(price)
if price >= 1.00:
    tax = .07
    print("The Tax rate is " + str(tax))
else:
    tax = 0
    print("The Tax rate is " + str(tax))