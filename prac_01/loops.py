for i in range(1, 21, 2):
    print(i, end=' ')
print()

for j in range(0, 100, 10):
    print(j, end=' ')
print()

for k in range(20, 0, -1):
    print(k, end=' ')
print()

stars = int(input("How many stars?: "))
for x in range(0, stars, 1):
    print("*", end=' ')
print()

for n in range(stars + 1):
    print("*" * n)
print()
