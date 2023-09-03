# Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

# The owner wants you to do some calculations on the data with these criteria's:

#     -calculate the total price average for all products

#     -create a new price list that reduces the old prices by $ 5

#     -calculate the total revenue generated from the products

#     -calculate the average daily revenue generated from the products

#     -based on the new prices, which products are less than $ 30 

# Below is the data you are to use for the problem :

# products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

# prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

# last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#SOLUTIONS
#1. Calculate the total prices
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
print(len(prices))
# #using sum()
# print("Total is: ", sum(prices))

# #using for loop with range
# Total=0
# for i in range(len(prices)):
#     Total=Total+prices[i]
#     print("The Total is:", Total)

#using for loop with range
# Total=0
# for i in prices:
#     Total=Total+i
#     print("The Total is:", Total)

#using while loop
Total=0
i=0
while (i < len(prices)):
    Total=Total+prices[i]
    i=i+1
print("The Total is:", Total)

Total_average_price = Total/(len(prices))
print("The total price average for all products: ", Total_average_price)
#below is to convert the answer to 2 decimal places
Total_average_price = "{:.2f}".format(Total_average_price)
print("The total price average for all products: ", Total_average_price)
#create a new price list that reduces the old prices by $ 5
old_prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

# #using while loop
# Total=0
# i=5
# for i in == 5:
#     new_price=old_prices-i
    
# print("The Total is:", new_price)
# old_prices =[0]- 5
# reduce_by = 5

# print((new_prices))