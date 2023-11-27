print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
n = int(input("Enter the number of Fibonacci numbers to generate: "))
a = 0
b = 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b