#Separate even and odd numbers

# Create a list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create empty lists for even and odd numbers
even = []
odd = []

# Check each number in the list
for num in numbers:

    # Check if the number is divisible by 2
    if num % 2 == 0:
        even.append(num)  # Add to even list
    else:
        odd.append(num)   # Add to odd list

# Display both lists
print("Even numbers:", even)
print("Odd numbers:", odd)








#Count prime numbers and create a new list
# Create a list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Create an empty list for prime numbers
prime = []

# Check each number in the list
for num in numbers:

    # Prime numbers must be greater than 1
    if num > 1:
        is_prime = True

        # Check whether the number is divisible
        # by any number from 2 up to num - 1
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break  # Stop checking if a divisor is found

        # Add the number if it is prime
        if is_prime:
            prime.append(num)

# Display prime numbers and their count
print("Prime numbers:", prime)
print("Count of prime numbers:", len(prime))














#Count happy numbers
# Create a list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Initialize the count
count = 0

# Check each number in the list
for num in numbers:

    # Store the number separately
    n = num

    # A happy number eventually reaches 1
    # An unhappy number eventually reaches 4
    while n != 1 and n != 4:
        total = 0

        # Find each digit and square it
        while n > 0:
            digit = n % 10
            total = total + digit * digit
            n = n // 10

        # Replace the number with the sum of squares
        n = total

    # If the result is 1, it is a happy number
    if n == 1:
        count = count + 1
        print(num, "is a happy number")

# Display the total count
print("Total happy numbers:", count)













# Get an integer from the user
num = int(input("Enter a number: "))

# Convert a negative number to positive
num = abs(num)

# Get the last digit using remainder
last = num % 10

# Keep removing the last digit
# until only the first digit remains
while num >= 10:
    num = num // 10

# Store the first digit
first = num

# Add the first and last digits
total = first + last

# Display the result
print("Sum of first and last digit:", total)








#Find all ways to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5 and Rs. 10 coins
# Initialize the number of combinations
count = 0

# Try 0 or 1 coin of Rs. 10
for ten in range(2):

    # Try different numbers of Rs. 5 coins
    for five in range(3):

        # Try different numbers of Rs. 2 coins
        for two in range(6):

            # Try different numbers of Rs. 1 coins
            for one in range(11):

                # Calculate the total value of the coins
                total = ten * 10 + five * 5 + two * 2 + one

                # Check if the total is exactly Rs. 10
                if total == 10:
                    count = count + 1

                    # Display the number of each coin
                    print("Rs. 10 coins:", ten,
                          "Rs. 5 coins:", five,
                          "Rs. 2 coins:", two,
                          "Rs. 1 coins:", one)

# Display the total number of combinations
print("Total ways:", count)










#Find duplicates in three lists

# Create three empty lists
list1 = []
list2 = []
list3 = []

# Ask how many elements each list should contain
n = int(input("Enter number of elements: "))

# Get elements for the first list
print("Enter first list:")
for i in range(n):
    num = int(input())
    list1.append(num)

# Get elements for the second list
print("Enter second list:")
for i in range(n):
    num = int(input())
    list2.append(num)

# Get elements for the third list
print("Enter third list:")
for i in range(n):
    num = int(input())
    list3.append(num)

# Create an empty list for common elements
duplicates = []

# Check each number in the first list
for num in list1:

    # Check if the number is present in both other lists
    if num in list2 and num in list3:

        # Avoid adding the same number more than once
        if num not in duplicates:
            duplicates.append(num)

# Display the common elements
print("Duplicates:", duplicates)













#Find the first non-repeating element in a list
# Create an empty list
numbers = []

# Ask the user for the number of elements
n = int(input("Enter number of elements: "))

# Get each number from the user
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Check each number in its original order
for num in numbers:

    # Count how many times the number appears
    if numbers.count(num) == 1:

        # Display the first number that appears once
        print("First non-repeating element:", num)
        break  # Stop after finding the first one

# Run this if the loop finishes without finding one
else:
    print("No non-repeating element found")












#Find the minimum element in a list# Create an empty list
numbers = []

# Ask the user for the number of elements
n = int(input("Enter number of elements: "))

# Get numbers from the user
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Assume the first element is the minimum
minimum = numbers[0]

# Compare every number with the current minimum
for num in numbers:

    # Update the minimum if a smaller number is found
    if num < minimum:
        minimum = num

# Display the smallest number
print("Minimum element:", minimum)

