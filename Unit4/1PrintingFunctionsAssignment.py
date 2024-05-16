# ========== 4.1.1 ==========
# def line (length, text):
#     if len(text) == 0:
#         print("*" * length)
#     else:
#         print(text[0:1] * length)
# line(7,"%")
# line(10, "LOL")
# line(3, "")
# ========== 4.1.2 ==========
# def box_of_hashes(width):
#     counter = 0
#     while True:
#         counter = counter + 1
#         print("#" * 10)
#         if counter == width:
#             break
# box_of_hashes(5)
# print (" ")
# box_of_hashes(2)
# ========== 4.1.3 ==========
# def square_of_hashes(width):
#     counter = 0
#     while True:
#         counter = counter + 1
#         print("#" * width)
#         if counter == width:
#             break
# square_of_hashes(5)
# print(" ")
# square_of_hashes(3)
# ========== 4.1.4 ==========
# def square(length, text):
#     counter = 0
#     while True:
#         counter = counter + 1
#         print(text * length)
#         if counter == length:
#             break
# square(5, "*")
# print(" ")
# square(3, "o")
# ========== 4.1.5 ==========
# def triangle(number, text):
#     counter = 1
#     while True:
#         print ("#" * counter)
#         counter = counter + 1 
#         if counter == number + 1:
#             break
# triangle(6, "#")
# print(" ")
# triangle(3, "#")
# ========== 4.1.6 ==========
# def shape(number1, shape1, number2, shape2):
#     counter = 1
#     while True:
#         if counter == number1 + 1:
#             break
#         print(shape1 * counter)
#         counter = counter + 1
#     counter2 = 0
#     while True:
#         if counter2 == number2:
#             break
#         print(shape2 * number1)
#         counter2 = counter2 + 1

# shape(5,"x", 3, "*")
# shape(2, "o", 4 , "+")
# shape(3, ".", 0, ",")
# ========== 4.1.7 ==========