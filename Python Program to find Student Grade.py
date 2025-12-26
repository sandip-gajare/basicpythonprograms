    #Python Program to find Student Grade

marks = float(input("Enter student marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
elif marks >= 40 and marks < 60:
    print("Grade: E")
elif marks >= 0 and marks < 40:
    print("Grade: F (Fail)")
else:
    print("Invalid Marks")