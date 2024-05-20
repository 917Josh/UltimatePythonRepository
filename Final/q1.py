fname = input("Please enter your first name:")
lname = input("Please enter your last name:")
gpa = float(input("Please enter your GPA:"))
pos = lname[0]
if gpa < 3.25:
    print("Hello, ", fname, ". You are eligible for a scholarship of $0.")
elif gpa >= 3.25 and gpa <= 3.49 :
    print("Hello, ", fname, ". You are eligible for a scholarship of $4000 ")
elif gpa >= 3.5 and gpa <= 3.69:
    print("Hello, ", fname, ". You are eligible for a scholarship of $8000")
elif gpa >= 3.7 and gpa <= 3.85:
     print("Hello, ", fname, ". You are eligible for a scholarship of $12000")
else:
    print("Hello, ", fname, ". You are eligible for a scholarship of $16000")