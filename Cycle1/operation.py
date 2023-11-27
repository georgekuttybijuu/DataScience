def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
def main():
    print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
    try:
        number = int(input("Enter a positive number: "))
        if number <= 0:
            print("Please enter a positive number.")
            return
        while number > 0:
            digit_sum = sum_of_digits(number)
            print(f"{number} - {digit_sum} = {number - digit_sum}")
            number = number - digit_sum
    except ValueError:
        print("Invalid input. Please enter a valid positive number.")
if __name__ == "__main__":
    main()
