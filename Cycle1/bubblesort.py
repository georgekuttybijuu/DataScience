def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
print("SJC22MCA-2027 - Georgekutty Biju\nS3MCA")
input_str = input("Enter elements separated by commas: ")
elements = [int(x) for x in input_str.split(',')]
bubble_sort(elements)
print("Sorted elements:", elements)
