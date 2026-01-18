def celcius_to_fahrenheit(c=0):
    return (c * 9 / 5) + 32


def main():
    try:
        user_input = input("Enter Celsius (press Enter for default 0): ").strip()
        if user_input == "":
            result = celcius_to_fahrenheit()
        else:
            result = celcius_to_fahrenheit(float(user_input))

        print(f"Fahrenheit: {result}")

    except ValueError:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()
