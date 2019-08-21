"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def calculate_fahrenheit():
    global fahrenheit
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def celsius_calcualator():
    global celsius
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        calculate_fahrenheit()
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius_calcualator()
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")

