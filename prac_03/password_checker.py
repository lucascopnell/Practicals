MIN_LENGTH = 4


def main():
    password = get_password()
    printing_password_asterisks(password)


def printing_password_asterisks(password):
    print(len(password) * "*")


def get_password():
    password = input("Please enter your password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid Password.")
        password = input("Please enter your password: ")
    return password


main()



