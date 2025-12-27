    #Python Program to find Total Average and Percentage of Five Subjects

# Input marks of five subjects
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

# Calculate total
total = m1 + m2 + m3 + m4 + m5

# Calculate average
average = total / 5

# Calculate percentage
percentage = (total / 500) * 100

# Display results
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
