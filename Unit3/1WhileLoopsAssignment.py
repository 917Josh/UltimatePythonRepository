# ========== 3.1.1 ==========
number = 2
print(number)
while True:
    number = number + 2
    print(number)
    if number == 30:
        break
# ========== 3.1.2 ==========
# print("Are you ready?")
# number = int(input("Please type in a number: "))
# while True:
#     print(number)
#     number = number - 1
#     if number == 0:
#         break
# print("Now!")
# ========== 3.1.3 ==========
# upperlimit = int(input("Upper limit"))
# current = 0
# while True:
#     current = current + 1
#     print (current)
#     if current == upperlimit:
#         break
# ========== 3.1.4 ==========
# upperlimit = int(input("Upper limit:"))
# current = 1
# while True:
#     print (current)
#     current = current * 2
#     if current >= upperlimit:
#         break
# ========== 3.1.5 ==========
upperlimit = int(input("Upper limit:"))
base = int(input("Base:"))
current = 1
while True:
    print (current)
    current = current * base
    if current >= upperlimit:
        break
# ========== 3.1.6 ==========
limit = int(input("Limit:"))
total = 0
current = 0
while True:
    current = current + 1
    total = total + current
    if total >= limit:
        break
print (total)