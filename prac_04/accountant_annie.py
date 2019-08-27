number_of_months = int(input("How many months?: "))
while 12 < number_of_months <= 0:
    print("Invalid entry.")
    number_of_months = int(input("How many months?: "))
for i in range(number_of_months):
    income_amount = float(input("How much income for month {}".format(number_of_months)))
