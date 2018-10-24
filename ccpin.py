#!/usr/bin/env python3
"""
This python module  use to simulate the bank card PIN number  check
"""
import sys

def valid_input():
    """
    This function use to check the validity of the PIN number.
    User will have 3 trials before the card got blocked
    """
    default_value = "1234"
    i = 1
    check = False
    """
    Check the conditions of user input
    """
    user_input = input("Enter your PIN number: ")
    while i !=3 and  check == False:
        """
        Check if user input has more or less than 4 digits
        """
        if(len(user_input)!=4):
            print("Invalid PIN length. Correct format is <9876>")
            user_input = input("Enter your PIN number: ")
            check = False
            i+=1
        elif(not user_input.isdigit()):
            print("Invalid PIN character. Correct format is <9876>")
            user_input = input("Enter your PIN number: ")
            check = False
            i+=1
        elif (user_input!=default_value):
            print("Your PIN number is incorrect")
            user_input = input("Enter your PIN number: ")
            check = False
            i+=1
        else:
            check = True
    """
    Return announcement of user card got blocked after 3 trials
    """
    if i==3:
        print("Your bank card is blocked")
    else:
        print("Your PIN is correct")



def main():
    """
    Test your module
    """
    valid_input()



if __name__ == "__main__":
    main()
    exit(0)

