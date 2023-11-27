print("SJC22MCA-2027 : Georgekutty Biju")
print("S3MCA")
n=int(input("enter the order :"))
m1=[]
print("enter the elements :")
for i in range(n):
    m1.append([])
    for j in range(n):
        num=int(input())
        m1[i].append(num)
m2=[]
print("enter the elements :")
for i in range(n):
    m2.append([])
    for j in range(n):
        num=int(input())
        m2[i].append(num)
print("first matrix is :")
for i in range(n):
    for j in range(n):
        print(m1[i][j],end=" ")
    print()
print("second matrix is :")
for i in range(n):
    for j in range(n):
        print(m2[i][j],end=" ")
    print()
m3=[]
for i in range(n):
    m3.append([])
    for j in range(n):
        m3[i].append(m1[i][j]+m2[i][j])
print("resultant matrix is :")
for i in range(n):
    for j in range(n):
        print(m3[i][j],end=" ")
    print()