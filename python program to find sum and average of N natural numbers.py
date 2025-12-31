# 1) Python Program to find Sum and Average of N Natural Numbers

'''n = int(input("enter a  number: "))

sum_n = n * (n + 1) // 2
average = sum_n / n

print("sum of first", n, " numbers =", sum_n)
print("average =", average)'''

# 2) Python Program to find Sum and Average of N Natural Numbers using for loop

'''n = int(input("enter a natural number: "))

sum_n = 0

for i in range(1, n + 1):
    sum_n = sum_n + i

average = sum_n / n

print("Sum of first", n, "natural numbers =", sum_n)
print("Average =", average)'''

# 3) Python Program to find Sum and Average of N Natural Numbers using while loop

n = int(input("enter a natural number: "))

sum_n = 0
i = 1

while i <= n:
    sum_n = sum_n + i
    i = i + 1

average = sum_n / n

print("Sum =", sum_n)
print("Average =", average)