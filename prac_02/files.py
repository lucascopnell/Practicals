out_file = open("data.txt", 'w')
name = input("Please enter your name: ")
print(name, file=out_file)
out_file.close()

name_file = open("data.txt", 'r')
name = name_file.read().strip()
name_file.close()
print("Your name is ", name)

numbers = open("numbers.txt", 'r')
number_1 = int(numbers.readline())
number_2 = int(numbers.readline())
print(number_1 + number_2)
numbers.close()

numbers = open('numbers.txt', 'r')
total = 0
for line in numbers:
    number = int(line.strip())
    total += number
print(total)
numbers.close()


