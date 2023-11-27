print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
s1=float(input("Enter first side: "))
s2=float(input("Enter second side: "))
s3=float(input("Enter third side: "))
if s1==s2==s3:
    print("Triangle is equilateral")
elif s1==s2 or s1==s3 or s2==s3 :
    print("Triangle is Issociless")
else:
    print("Triangle is Scalene")