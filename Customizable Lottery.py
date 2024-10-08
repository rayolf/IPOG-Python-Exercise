# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TNoJ1wq64zF5f_0gDwG-YYEPes0DxCId
"""

# Evaluation Activity (Programming Logic)

# You will play a small 'customizable lottery' game in Python.
# THE RULES ARE AS FOLLOWS: You will choose the first and last number,
# generating the range for the draw. The difference between these two numbers must be
# at least 10. For example, selecting the first number 1, the last must be at least 11.
# After defining the 'range' of numbers for the draw, choose
# your bet number. Your number must be within the previously defined 'range'.
# If the drawn number is your chosen one, you win!

import random
#---
numbers_range = []
#---
play_again = True
greater_than_zero = False
greater_than_ten_units = False
within_range = False
response_options = False
#---
def reset_conditions():
    global numbers_range, play_again, greater_than_zero
    numbers_range = []
    play_again = True
    greater_than_zero = False
#---
while play_again:
    while not greater_than_zero:
        initial_number = int(input('Enter the first number of the draw range. It must be greater than zero: '))
        if initial_number > 0:
            greater_than_zero = True
            print("\nThank you. Now choose the last number of the draw range\nNote: It must be at least ten units greater than the first.\n")
            greater_than_ten_units = False
        else:
            print("You did not choose a number greater than zero.\n")
#---
    while not greater_than_ten_units:
        final_number = int(input('Enter the last number of the draw range: '))
        if final_number - initial_number >= 10 and final_number > 0:
            greater_than_ten_units = True
            for i in range(initial_number, final_number + 1):
                numbers_range.append(i)
            print("\nThank you. Now choose the number you want to bet on. It must be one of the numbers below.")
            print(f"These are the numbers that will participate in the draw: {numbers_range}")
            within_range = False
        else:
            if final_number <= 0:
                print("\nYou did not choose a number greater than zero.")
            print("The difference between the first and last number was not equal to or greater than ten.\n")
    #---
        while not within_range and greater_than_ten_units:
            bet_number = int(input('\nEnter the number you want to bet on: '))
            if bet_number in numbers_range:
                within_range = True
                drawn_number = random.choice(numbers_range)
                hit = bet_number == drawn_number
                message = f"\nYour bet number was {bet_number} and the drawn number was {drawn_number}. Congratulations, you hit the jackpot!" if hit else f"\nThe drawn number was {drawn_number}, but your bet number was {bet_number}. Better luck next time!"
                print(message)
                if not hit:
                    response_options = False
                    while not response_options:
                        play_response = input("\nDo you want to bet again?\nType yes or no: ")
                        if play_response == "yes":
                            print("\nAlright! Let's play again.\n")
                            response_options = True
                            #---
                            reset_conditions()
                            #---
                        elif play_response == "no":
                            print("\nThank you for playing!")
                            play_again = False
                            response_options = True
                        else:
                            print("\nPlease type yes or no.")
                else:
                    play_again = False
        #---
            else:
                print("The bet number is not within the draw range.\n")
#----