def celsius_to_fahrenheit(c=0):
    return (c * 9 / 5) + 32


if __name__ == "__main__":
    user_input = input("Enter Celsius (press Enter for default 0): ")
    if user_input.strip() == "":
        print(celsius_to_fahrenheit())
    else:
        print(celsius_to_fahrenheit(float(user_input)))
