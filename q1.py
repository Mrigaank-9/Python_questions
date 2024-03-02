# Question number 1 
''' Guess the aplhabet'''
from Check_guess import check_guess
import random

def assumption_check(limit_to_check): # checks if the input is proper or not 
    if(len(limit_to_check)>1):
        print("Wrong input")
        return False
    elif(ord(limit_to_check)<97 or ord(limit_to_check)>122):
        print("Wrong Input")
        return False
    return True

point = 0 
random_char = chr(random.randint(97, 123))
# print(f"The Random Character : {random_char}")
for i in range(0,3):
    user_input = input("Enter an alphabet to guess: ")
    user_input = user_input.lower()
    if (assumption_check(user_input)==False) : 
        continue
    flag_found = False     # flag to check if found character is found or not
    checking_guess_by_calling_check_guess_function = check_guess(user_input,random_char)
    if(checking_guess_by_calling_check_guess_function==0):
        flag_found = True
        if(i == 0):
            point = 26 
        elif(i == 1):
            point = 13 
        else:
            point = 7

    if(flag_found): # thsi if will only work if the character is found else loop will go on
        break
            
print(f"\nTotal Points: {point}")
print(f"The Random Character : {random_char}")

