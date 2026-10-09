#Separate even and odd numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

#Count prime numbers and create a new list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

prime = []

for num in numbers:
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime.append(num)

print("Prime numbers:", prime)
print("Count of prime numbers:", len(prime))



#Count happy numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

count = 0

for num in numbers:
    n = num

    while n != 1 and n != 4:
        total = 0

        while n > 0:
            digit = n % 10
            total = total + digit * digit
            n = n // 10

        n = total

    if n == 1:
        count = count + 1
        print(num, "is a happy number")

print("Total happy numbers:", count)



#Find the sum of the first and last digit

num = int(input("Enter a number: "))

num = abs(num)
last = num % 10

while num >= 10:
    num = num // 10

first = num

print("Sum of first and last digit:", first + last)



#Find all ways to make Rs. 10 using Rs. 1, Rs. 2, Rs. 5 and Rs. 10 coins
count = 0

for ten in range(2):
    for five in range(3):
        for two in range(6):
            for one in range(11):

                total = ten * 10 + five * 5 + two * 2 + one

                if total == 10:
                    count = count + 1

                    print("Rs. 10 coins =", ten,
                          "Rs. 5 coins =", five,
                          "Rs. 2 coins =", two,
                          "Rs. 1 coins =", one)
                    print()

print("Total number of ways =", count)




#Find duplicates in three lists

list1 = []
list2 = []
list3 = []

n = int(input("How many elements in each list? "))

print("Enter first list elements:")
for i in range(n):
    num = int(input())
    list1.append(num)

print("Enter second list elements:")
for i in range(n):
    num = int(input())
    list2.append(num)

print("Enter third list elements:")
for i in range(n):
    num = int(input())
    list3.append(num)

duplicates = []

for num in list1:
    if num in list2 and num in list3:
        if num not in duplicates:
            duplicates.append(num)


print("Duplicates:", duplicates)



#Find the first non-repeating element in a list
numbers = []

n = int(input("How many elements? "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

for num in numbers:
    if numbers.count(num) == 1:
        print("First non-repeating element:", num)
        break
else:
    print("No non-repeating element found")



#Find the minimum element in a list
numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum element:", minimum)

