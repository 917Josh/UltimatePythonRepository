# print("########## 2.2.1 ##########")
# age = int(input("What is your age?"))
# if age <= 5 and age >= 0:
#     print ("I suspect you can't write quite yet...")
# elif age <= -1:
#     print ("That must be a mistake")
# else:
#     print("Ok, you're ", age, "years old")
# print("########## 2.2.2 ##########")
# name = input("Please type in your name:")
# if name == "morty":
#     print("I think you might be one of Mickey Mouse's nephews.")
# elif name == "huey":
#     print("I think you might be one of Donald Duck's nephews.")
# else:
#     print("You're not a nephew of any character I know of.")
# print("########## 2.2.3 ##########")
# percent = int(input("Print in percent:"))
# if percent >= 0 and percent <= 59:
#     print ("F")
# elif percent >= 60 and percent <= 69:
#     print ("D")
# elif percent >= 70 and percent <= 79:
#     print ("C")
# elif percent >= 80 and percent <= 89:
#     print ("B")
# elif percent >= 90 and percent <= 100:
#     print ("A")
# else:
#     print("impossible!")
# print("########## 2.2.4 ##########")
# number = int(input("Number:"))
# if number % 3 == 0 and number % 5 == 0:
#     print ("fizzbuzz")
# elif number % 3 == 0:
#     print ("fizz")
# elif number % 5 == 0:
#     print ("buzz")
# print("########## 2.2.5 ##########")
# year = int(input("Please type in a year:"))
# if year % 4 == 0:
#     print ("That year is a leap year")
# elif year % 400 == 0:
#     print("That is a leap year")
# else:
#     print ("That is not a leap year")
# print("########## 2.2.6 ##########")
letter1 = input("1st letter:")
letter2 = input("2nd letter:")
letter3 = input("3rd letter:")

if letter1 > letter3:
    if letter2 > letter3:
        if letter1 > letter2:
            print("The letter in the middle is", letter2)
        else:
            print("The letter in the middle is", letter1)
    else:
        print ("The letter in the middle", letter3)
else:
    if letter2 > letter1:
        print("The letter in the middle is", letter1)
    else:
        if letter2 > letter3:
            print ("The letter in the middle is", letter2)
        else:
            print ("The letter in the middle is", letter3)