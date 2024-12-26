size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    # Use a for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")  
    print()  
    row += 1
