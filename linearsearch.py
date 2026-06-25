# Get number of elements
n = int(input("Enter number of elements: "))

# Create list
lst = []

# Get elements from user
for i in range(n):
    value = int(input("Enter element: "))
    lst.append(value)

# Get target value
target = int(input("Enter target value to search: "))

# Search target in list
if target in lst:
    print("Target value found at index", lst.index(target))
else:
    print("Target value not found")