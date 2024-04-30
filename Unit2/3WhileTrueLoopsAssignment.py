# ========== 2.3.1 ==========
while True:
    print ("hi")
    answer = input("Shall we continue? ")
    if answer == "no":
        break      
print ("okay then")
# ========== 2.3.2 ==========
from math import sqrt
while True: 
    number = int(input("Countdown!"))
    if number == 0:
        break
    elif number < 0:
        print("The square root of", number, "is", sqrt(number))
print({"Exiting..."})
# ========== 2.3.3 ==========
number=int(input("Countdown"))
while True:
    print(number)
    if number == 0:
        break
    number = number-1
print("Now!")
# ========== 2.3.4 ==========
password=input("Password")
repeat=input("repeat password")
while True:
    if password==repeat:
        break
    print("They do not match!")
    repeat=input("repeat password:")
print("user account created")
# ========== 2.3.5 ==========
pin=int(input("Pin:"))
tries = 1
while True:
    if pin==4321:
        break
    print("wrong")
    tries = tries+1
    pin=int(input("Pin:"))
print("Correct, it took you", tries, "tries.")
# ========== 2.3.6 ==========
# ========== 2.3.7 ==========
story = ""
while True:
    word = input("Please type in a word")
    if word == "End":
        break
    story = story + " " + word
print(story)
# ========== 2.3.8 ==========
story = ""
lastword = ""
while True:
    word = input("Please type in a word:")
    if word == "end":
        break
    if word == lastword:
        break
    story = story + " " + word
    lastword = word
print(story)
# ========== 2.3.9 ==========
count = 0
sum = 0
mean = 0
positive = 0
negative = 0
while True:
    number=int(input("Number:"))
    if number == 0:
        break
    count = count + 1
    sum = sum + number
    mean = sum / count
    if number > 0:
        positive = positive
    else:
        negative = negative + 1
print ("Number typed in:", count)
print("Sum of numbers:", sum)
print("Mean of numbers:", mean)
print ("Positive numbers:", positive)
print("Negative numbers:", negative)

