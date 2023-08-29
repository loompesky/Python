#TipCalculator is a program to calculate the total amount of a meal purchased with a fixed tip

# As the finance officer of Asanka Hotel, the food and beverages director has requested a program that calculates the total amount of a meal purchased with a fixed tip. 
# Below are the requirements for the program:
# The program should ask the user to enter the charge for the food.
# It should then calculate the amounts of an 18 percent tip and 7 percent sales tax on the charge of the food and display each of these amounts.
# Finally, it should add everything together and display the charge of the food plus tip and sales tax.
# Based on this data, your program should generate script that meets the requirements.  
# Below is an example execution of the program: 
# input
# Charge for food = $50.00
# output
# Tip = $9.00
# Sales tax = $3.50
# Grand total = $62.50


#The program should ask the user to enter the charge for the food
food_charge = input ("Please enter the charge for the food: ")
print()
tip = 0.18 * float(food_charge)
print("An amounts of 18 percent tip on the food charge is: $" + str(tip))
sales_tax = 0.07 * float(food_charge)
#below is to convert the answer to 2 decimal places
sales_tax = "{:.2f}".format(sales_tax)
print("An amounts of 7 percent sales tax on the food charge is: $" + str(sales_tax))
total =  float(tip) + float(sales_tax)
print("The grand total is: $", float(total) + float(food_charge))
