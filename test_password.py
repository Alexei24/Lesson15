import task0101

def main():
    password = input("Enter your password: ")

    result = task0101.check_password(password)

    msg = f"Your password is {result}" if isinstance(result, str) else "User invalid data"

    print(msg)


if __name__ == "__main__":
    main()