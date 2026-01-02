#Python Program to Find Sum of 10 Numbers until user enters Positive Numbers

count = 0
total = 0

print("enter numbers (only positive numbers will be counted):")

while count < 10:
    num = int(input("enter a number: "))

    if num > 0:
        total += num
        count += 1
    else:
        print("Negative number ignored!")

print("Sum of 10 positive numbers =", total)