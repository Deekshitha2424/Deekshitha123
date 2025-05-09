# Python program to print numbers in triangular form using for loop

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(rows - i + 1):
        print(i, end=" ")
    print()
