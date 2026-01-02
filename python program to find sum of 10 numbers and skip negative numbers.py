#Python Program to Find Sum of 10 Numbers and Skip Negative Numbers

total = 0

print("enter 10 numbers:")

for i in range(1, 11):
    num = int(input(f"enter number {i}: "))

    if num < 0:
        continue   # skip negative numbers

    total += num

print("sum of positive numbers =", total)