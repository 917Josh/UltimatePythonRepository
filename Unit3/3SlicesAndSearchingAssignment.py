# ========== 3.3.1 ==========
# string = input("Please type in a string:")
# endpos = 1
# while True:
#     print(string[:endpos])
#     endpos = endpos + 1
#     if len(string) + 1 == endpos:
#         break
# ========== 3.3.2 ==========
# string = input("Please type in a string:")
# startpos = len(string) - 1
# while True:
#     print(string[startpos:len(string)])
#     startpos = startpos - 1
#     if startpos == -1:
#         break
# ========== 3.3.3 ==========
# string = input("Please type in a string:")
# if (string.find("a") >= 0):
#     print ("a found")
# else: 
#     print("a not found")
# if (string.find("e") >= 0):
#     print ("e found")
# else: 
#     print("e not found")
# if (string.find("o") >= 0):
#     print ("o found")
# else:
#     print("o not found")
# ========== 3.3.4 ==========
# word = input("Please type in a word:")
# letter = input("Please type in a character:")
# foundpos = word.find(letter)
# print(word[foundpos:foundpos + 3])
# ========== 3.3.5 ==========
# word = input("Please type in a word:")
# character = input("Please type in a character:")
# foundpos = word.find(character)
# print(word[foundpos:foundpos + 3])
# ========== 3.3.6 ==========
string = input("Please type in a string:")
substring = input("Please type in a substring:")
if string.find(substring) < 0:
    print("The substring does not occur in the string")
else:
    remaining = string[string.find(substring) + 1:len(string)]
    first = string.find(substring)
    if remaining.find(substring) < 0:
        print("The substring does not occur twice in the string.")
    else:
        second = remaining.find(substring) 
        index = first + second + 1 
        print("The second occurence of the substring is at index ", index)