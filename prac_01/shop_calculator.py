number_of_items = int(input("How many items do you have?: "))
while number_of_items < 0:
    print("Invalid Number of Items")
    number_of_items = int(input("How many items do you have?: "))
total = 0
for i in range(number_of_items):
    price = float(input("Enter the price of your item" + str(i) + ": "))
    total += price
if total > 100:
    total *= 0.9
print("Total Price is: ", total)
