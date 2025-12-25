                        #basic python program 

'''print("hello world")

#add two numbers 
print(5 + 5)

a=5
b=10
c=a+b
print(c)

#subtract two numbers
print(8 - 4)

a=9
b=3
c=a-b
print(c)'''

#how to use arithmetic operator
'''num1=float(input("enter the frist number :"))
num2=float(input("enter the second number :"))

#add two numbers
add=num1+num2
print("addition is :=",add)

#subtract two numbers
sub=num1-num2
print("subtraction is :=",sub)

#multiply two numbers
mul=num1*num2
print("multiplication is :=",mul)

#divided two numbers
div=num1/num2
print("division is :=",div)

#modulus two numbers
mod=num1%num2
print("modulus is :=",mod)'''

#python calendar example
'''import calendar
year=int(input("enter the year number :"))
month=int(input("enter the month number :"))

print(calendar.month(year,month))'''

#Python Program to find Largest of 2 Numbers using Elif Statement
'''a=int(input("enter the first value a:"))
b=int(input("enter yhe second value b:"))

if(a>b):
    print("{0} is Greater than {1}".format(a, b))
elif(b > a):
    print("{0} is Greater than {1}".format(b, a))
else:
    print("Both a and b are Equal")'''

#Python Program to find Largest of 3 Numbers using Elif Statement
'''a = float(input(" Enter the First value: "))
b = float(input(" Enter the First value: "))
c = float(input(" Enter the First value: "))

if (a > b and a > c):       #How to use if statement in python
    print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
    print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
    print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
    print("Either any two values or all the three values are equal")'''

#Python Program to Check Leap Year
'''year = int(input("enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  #agar sal 4 se (divisible) ho — to vah संभावित(potentially) leap year है।
    print(f"{year} is a leap year")  #f-string vah string hai jisame aap {} ka upayog karke variables or expressions ko sidhe string ke ander likh sakte hai
else:
    print(f"{year} is not leap year")'''

#Python Program to Print Negative Numbers in a Range
'''start = int(input("enter the strting value: "))
end = int(input("enter the ending value: "))

print("all negative numbers from:")
for num in range(start, end + 1): #range(start, end+1) start se lekar end tak sabhi numbers generate karta hai
    if num < 0:                   #end + 1 esiliye, क्योंकि Python me range ending number ko exclude karta hai
        print(num)'''

#Python Program to Print Positive Numbers in a Range
'''start = int(input("enter the strting value: "))
end = int(input("enter the ending value: "))

print("all positive numbers from:")
for num in range(start, end + 1): 
    if num > 0:        #yah condition check karti hai ki present number positive hai ya nahi           
        print(num)'''

#Python Program to check Number is Positive or Negative
'''num = float(input("enter any numeric value: "))

# positive/negative/zero check karna
if num > 0:
    print(f"{num} is a positive number") #f-string ka upayog karke number or message ko ek sath print karta hai, jese 5.0 ek Positive number hai
elif num < 0:
    print(f"{num} is a negative number")
else:
    print("You have entered Zero")'''

#Python Program to Check Number is Divisible by 5 and 11
'''num = int(input("enter a number: "))

if num % 5 == 0 and num % 11 == 0:  #'and' ka  matalbe dono conditions true hona chahiye tabhi pura condition True hoga
    print(f"{num} The number is divisible by both 5 and 11")
else:
    print(f"{num} The number is not divisible by both 5 and 11")'''

#Python Program to Find the Sum and Average Of Three Numbers
'''a = float(input("enter the first value : "))
b = float(input("enter the second value: "))
c = float(input("enter the third value: "))

total = a + b + c
average = total / 3

print(f"Sum = {total}")
print(f"Average = {average:.2f}")   #Show the meaning of {average:.2f} by formatting the average to 2 decimal places '''

#Python Program to Find the Average Of Two Numbers
'''num1 = 10
num2 = 20

average = (num1 + num2) / 2

print("Average =", average)'''

#How to use user input
'''num1 = float(input("enter the first value: "))
num2 = float(input("enter the second value: "))

average = (num1 + num2) / 2

print("Average =", average)'''

#python program to get current date
'''from datetime import date

current_date = date.today()

print("Current Date =", current_date)'''

#python program to get current time
'''from datetime import datetime

current_time = datetime.now().time()

print("Current Time =", current_time)'''

#Python Program to Get Current Date and Time
from datetime import date

today = date.today()
print("Current Date = ", today)






