#Python Program to calculate Sum of Series 1²+2²+3²+….+n²

n = int(input("enter the value of n: "))

sum_of_squares = 0

for i in range(1, n + 1):
    sum_of_squares += i * i

print("Sum of the series 1² + 2² + 3² + ... +", n, "² is:", sum_of_squares)