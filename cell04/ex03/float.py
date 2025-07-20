# This program checks if a number is an integer or a decimal
# It prompts the user to input a number and then checks its type
num = float(input("Give me a number: "))
if int(num) == num:
    print("This number is an integer")  # แสดงผลว่าเป็นจำนวนเต็ม
else:
    print("This number is a decimal")   # แสดงผลว่าเป็นจำนวนทศนิยม
