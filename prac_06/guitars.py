from prac_06.guitar import Guitar

print("My Guitars!")

guitars = []
guitar_name = input("Name: ")
while guitar_name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar = Guitar(guitar_name, year, cost)
    guitars.append(new_guitar)
    print("{} ({}) : {:,.2f} added".format(new_guitar.name, new_guitar.year, new_guitar.cost))
    guitar_name = input("Name: ")

print("These are my guitars!")
list_of_guitars = [str(guitar) for guitar in guitars]
print(list_of_guitars)
for i, guitar in enumerate(guitars):
    print("Guitar {}: {:>2} ({}), worth ${:,.2f} , vintage: {}".format(i + 1, guitar.name, guitar.year, guitar.cost, guitar.is_vintage()))