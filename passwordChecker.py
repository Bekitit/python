def main():
    password = input("Insert password: ")

    if password.isupper():
        print("Try again.")
        main()
    elif password.islower():
        print("Try again.")
        main()
    elif password.isdigit():
        print("Try again.")
        main()
    elif password.isalpha():
        print("Try again.")
        main()
    else:
        print("Password accepted")

main()
