# ========== 4.2.1 ==========
# def greatest_number(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#        return(num1)
#     elif num2 > num1 and num2 > num3:
#         return(num2)
#     else:
#         return(num3)
# print(greatest_number(3, 4, 1))
# print(greatest_number(99, -4, 7))
# print(greatest_number(0, 0, 0)) 
# ========== 4.2.2 ==========
def same_chars(word, index1, index2):
    # check here if index1 or index2 is too large!
    if index1 > len(word) or index2 > len(word):
        return("the second index is not within the string")

    letter1 = word[index1]
    letter2 = word[index2]

    # now, check if they're equal
    if letter1 == letter2:
        return("True")
    elif index1 > len(word) or index2 > len(word):
        return("the second index is not within the string")
    else:
        return("False")
    
print(same_chars("programmer", 6, 7)) # True
print(same_chars("programmer", 0, 4)) # False
print(same_chars("programmer", 0, 12)) # False
# ========== 4.2.3 ==========



