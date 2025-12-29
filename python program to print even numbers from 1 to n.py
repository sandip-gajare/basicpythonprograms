# 1) python program to print even numbers from 1 to N

'''n = int(input("enter a number: "))

print("even numbers from 1 to", n, "are:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)'''

# 2) Python Program to display Even Numbers using While Loop

n = int(input("enter a number: "))

i = 1
print("even numbers from 1 to", n, "are:")
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1