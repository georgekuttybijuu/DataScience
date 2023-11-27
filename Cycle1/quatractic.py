import cmath
def quadratic_roots(a,b,c):
   disc=b**2 - 4*a*c
   root1=(-b + cmath.sqrt(disc)) / (2*a)
   root2=(-b - cmath.sqrt(disc)) / (2*a)
   root1 = round(root1.real,2) + round(root1.imag,2) * 1j
   root2 = round(root2.real,2) + round(root2.imag,2) * 1j
   return root1,root2
print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
a=float(input("Enter the coefficient of a: "))
b=float(input("Enter the coefficient of b: "))
c=float(input("Enter the coefficient of c: "))
roots = quadratic_roots(a,b,c)
print("Roots of the quadratic equation are: ",roots)
