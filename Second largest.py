
numbers = [10, 25, 8, 45, 30]

# Remove duplicates and sort
unique_numbers = list(set(numbers))
unique_numbers.sort()

# Second largest number
second_largest = unique_numbers[-2]

print("Second Largest Number:", second_largest)