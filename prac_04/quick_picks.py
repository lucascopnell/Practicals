import random

NUMBERS_EACH_LINE = 6
MIN = 1
MAX = 45


def main():
    number_quick_picks = int(input("How many quick picks would you like?: "))
    while number_quick_picks < 0:
        print("Please choose a different quick pick.")
        number_quick_picks = int(input("How many quick picks would you like?: "))
    for i in range(number_quick_picks):
        quick_picks = []
        for j in range(NUMBERS_EACH_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_picks:
                number = random.randint(MIN, MAX)
            quick_picks.append(number)
        quick_picks.sort()
        print("".join("{:3}".format(number) for number in quick_picks))



main()


