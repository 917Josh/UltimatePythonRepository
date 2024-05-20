cost = 50
print("Amount due:", cost)
while True:
    insertcoin = int(input("Insert coin:"))
    amountdue = cost - insertcoin
    amntdue = amountdue - insertcoin
    if amountdue != 0:
        print("Amount due:", amountdue)
    elif amountdue == 0:
        print("Change owed:", amountdue * -1)
        break