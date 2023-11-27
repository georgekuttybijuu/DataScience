print("SJC22MCA-2027-Georgekutty Biju\nS3MCA")
list1 = input("Enter the first list of numbers separated by spaces: ").split()
list2 = input("Enter the second list of numbers separated by spaces: ").split()
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]
result = []
if len(list1) == len(list2):
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    print("Result of element-wise addition:", result)
else:
    print("Lists must have the same length for element-wise addition.")