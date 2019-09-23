
from prac_06.guitar import Guitar

my_guitar = Guitar("guitar_test", 1940, 16005.56)
print("{} get_age() - Expected 79 got {}".format(my_guitar.name, my_guitar.get_age()))
print("{} is_vintage() - Expected True got {}".format(my_guitar.name, my_guitar.is_vintage()))

