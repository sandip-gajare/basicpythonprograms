                            #Python Math Programs

#Python Program to find Cube of a Number
#step1
'''num = int(input("Enter a number: "))
cube = num * num * num      #yaha number ko 3 bar multiply kiya gaya hai yah cube nikalneka ka tarika hai
print("Cube of the number is:", cube)'''

#step2
'''num = int(input("Enter a number: "))
cube = num ** 3
print("Cube of the number is:", cube)'''

#Python Program to Calculate Profit or Loss using elif Statement
'''cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:      #agar Selling Price > Cost Price hai to Profit
    profit = selling_price - cost_price     #Profit calculate kiya gaya
    print("You a profit of:", profit)

elif selling_price < cost_price:     #agar Selling Price < Cost Price hai to Loss
    loss = cost_price - selling_price       #Loss calculate kiya gaya
    print("You a loss of:", loss)

else:
    print("No Profit, No Loss")'''

#Python Program to Calculate Square of a Number
#example1
'''num = int(input("Enter a number: "))
square = num * num
print("Square of the number is:", square)'''

#example2
'''number = float(input(" enter a number : "))
square = number ** 2
print(" Square of the Number is : {0}  = {1}".format(number, square))'''

#example3  Python Program to find Square of a Number using Functions
'''def square(num):        #def keyword function banane ke liye hota hai , #square function ka name hai
    return num * num    #number ko khud se multiply kiya gaya hai

number = int(input("Enter a number: "))
result = square(number)     #square() function call kiya gaya hai
print("Square of the number is:", result)'''

#Python Program to find Square root of a Number
#example1 Using math.sqrt() Function
'''import math     #Python ka built-in module hai, esame sqrt() function available hota hai

num = float(input("Enter a number: "))  #float() esaliye use kiya gaya taki decimal numbers bhi accept ho
result = math.sqrt(num)     #sqrt() function square root nikalta hai
print("Square root of the number is:", result)'''

#example2 Using Power Operator (**)
'''num = float(input("Enter a number: "))
result = num ** 0.5     #0.5 matlbe power 1 ka aadha hota hai
print("Square root of the number is:", result)'''

#Python Program to find all divisors of an integer
#example 1 Using Loop
'''num = int(input("Enter a number: "))

print("Divisors of", num, "are:")   #divisors hamesha positive integers hote hai

for i in range(1, num + 1):
    if num % i == 0:        #% modulus operator remainder check karta hai, remainder 0 hai to i divisor hai
        print(i)'''

#example 2 Using Function
'''def findDivisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)

num = int(input(" enter any number to find divisors = "))
findDivisors(num)'''

#Python Program to Calculate Compound Interest
'''P = float(input("Enter Principal Amount: "))    #P matlbe:- Principal Amount
R = float(input("Enter Rate of Interest: "))    #R matlbe:- Rate of Interest (per year)
T = float(input("Enter Time (in years): "))     #T matlbe:- Time

A = P * (1 + R / 100) ** T      #Compound interest ka formula apply kiya hai, ** T matlbe power of time
CI = A - P      #Final Amount se Principal Amount (-) subtract kiya gaya
print("Final Amount is:", A)    #A matlbe:- Final Amount
print("Compound Interest is:", CI)'''

#Python Program to Calculate Electricity Bill
'''units = int(input("Enter total electricity units: "))
bill = 0        #bill amount store karne ke liye
if units <= 100:
    bill = units * 5

elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
print("Total Electricity Bill is: ", bill)'''

#Python Program to Find Distance Between Two Points
'''import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between two points is:", distance)'''

#Python Program to find Power of a Number
#example 1 Using Power Operator (**)
'''number = int(input(" enter any positive integer : "))
exponent = int(input(" enter exponent value : "))
power = 1
for i in range(1, exponent + 1):
    power = power * number  
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))'''

#example 2 Using While Loop
'''number = int(input(" enter any positive integer : "))
exponent = int(input(" enter exponent value : "))
power = 1
i = 1
while(i <= exponent):
    power = power * number
    i = i + 1  
print("The result of {0} power {1} = {2}".format(number, exponent, power))'''

#example 3 Program to find the Power of a Number using pow function
'''import math

number = int(input(" Please Enter any Positive Integer : "))
exponent = int(input(" Please Enter Exponent Value : "))
power = math.pow(number, exponent)   
print("The Result of {0} Power {1} = {2}".format(number, exponent, power))'''

#Python Program to Print Multiplication Table
#example 1 using for loop
'''num = int(input("enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)'''

#example 2 using while Loop
'''num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1'''

#example 3 using ested for loop
num = int(input(" enter a number : "))
print(" Multiplication Table ")

for i in range(num, 11):
    for j in range(1, 11):
        print('{0}  *  {1}  =  {2}'.format(i, j, i*j))
    print('==============')
