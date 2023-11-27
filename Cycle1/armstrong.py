print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
def armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    digit_sum = sum(int(digit) ** num_digits for digit in num_str)
    return digit_sum == num
for num in range (1,1001):
    if armstrong(num):
        print(num)