import random
print(random.randint(5, 20))

# Question 1: Random number generated each time between 5 and 20, inclusive of 5 and 20.
# Question 2: The smallest number was 5 and the largest was 20.

print(random.randrange(3, 10, 2))

# produces a number between 3 and 10 exclusive of 10 which have steps of 2 between each number.
# 3 was the smallest, 9 was the largest
# No as it will produce a step greater than 2

print(random.uniform(2.5, 5.5))

# it produced a random number generator of float numbers to 15 decimal places
# The smallest number that could be seen would be 2.5 and the greatest number is 5.5, depending on rounding.



