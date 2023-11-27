def find_absent_digits(mobile_number):
    all_digits = set("0123456789")
    number_digits = set(mobile_number)
    return all_digits - number_digits
def main():
    print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
    mobile_number = input("Enter a 10-digit mobile number: ")
    if len(mobile_number) != 10 or not mobile_number.isdigit():
        print("Please enter a valid 10-digit mobile number.")
        return
    absent_digits = find_absent_digits(mobile_number)
    if absent_digits:
        print("Digits absent in the mobile number:", ", ".join(absent_digits))
    else:
        print("All digits are present in the mobile number.")
if __name__ == "__main__":
    main()
