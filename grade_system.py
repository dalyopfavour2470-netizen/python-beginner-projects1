print("Grade Calculator")

score = float(input("Enter student score (0-100): "))

if score >= 70:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
elif score >= 45:
    print("Grade: D")
else:
    print("Grade: F")