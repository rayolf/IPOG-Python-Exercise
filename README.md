# Customizable Lottery Game

This repository contains a Python project where you can play a 'customizable lottery' game. The project was developed as part of an evaluation activity for a **Programming Logic** course. The game allows you to choose a range of numbers and place a bet on a number within that range, with specific rules for the range and betting process.

## Game Rules

- You will be asked to choose the **first** and **last** number to define a range for the lottery draw.
- The difference between the **first** and **last** number must be at least 10.
  - For example, if you select **1** as the first number, the last number must be at least **11**.
- After defining the range, you will place a bet by choosing a number within that range.
- A random number will be drawn from the range, and if it matches your bet, you win!

## Code Explanation

The program follows these steps:

1. **Range Definition**: 
   - The player is asked to enter the first and last numbers to create a range of numbers.
   - The last number must be at least 10 units greater than the first, otherwise, the player will be prompted to try again.

2. **Bet Placement**:
   - After defining the range, the player is prompted to select a number to bet on, which must be within the previously defined range.

3. **Random Draw**:
   - The program randomly selects a number from the defined range using Python’s `random.choice()` function.
   - If the randomly drawn number matches the player's bet, the player wins.

4. **Game Continuation**:
   - If the player wins, the game ends.
   - If the player loses, they are asked whether they want to play again. They can continue betting or choose to exit the game.

## Code Structure

```python
import random

# List to hold the range of numbers
numbers_range = []

# Boolean flags for game conditions
play_again = True
greater_than_zero = False
greater_than_ten_units = False
within_range = False
response_options = False

# Function to reset conditions for replay
def reset_conditions():
    global numbers_range, play_again, greater_than_zero
    numbers_range = []
    play_again = True
    greater_than_zero = False

# Main game loop
while play_again:
    # Step 1: Get the initial number greater than zero
    while not greater_than_zero:
        initial_number = int(input('Enter the first number of the draw range. It must be greater than zero: '))
        if initial_number > 0:
            greater_than_zero = True
            print("\nThank you. Now choose the last number of the draw range\nNote: It must be at least ten units greater than the first.\n")
            greater_than_ten_units = False
        else:
            print("You did not choose a number greater than zero.\n")
    
    # Step 2: Get the final number that is at least 10 units greater than the initial
    while not greater_than_ten_units:
        final_number = int(input('Enter the last number of the draw range: '))
        if final_number - initial_number >= 10 and final_number > 0:
            greater_than_ten_units = True
            # Generate the number range
            for i in range(initial_number, final_number + 1):
                numbers_range.append(i)
            print("\nThank you. Now choose the number you want to bet on. It must be one of the numbers below.")
            print(f"These are the numbers that will participate in the draw: {numbers_range}")
            within_range = False
        else:
            if final_number <= 0:
                print("\nYou did not choose a number greater than zero.")
            print("The difference between the first and last number was not equal to or greater than ten.\n")
    
    # Step 3: Betting and random draw
    while not within_range and greater_than_ten_units:
        bet_number = int(input('\nEnter the number you want to bet on: '))
        if bet_number in numbers_range:
            within_range = True
            drawn_number = random.choice(numbers_range)
            hit = bet_number == drawn_number
            message = (f"\nYour bet number was {bet_number} and the drawn number was {drawn_number}. Congratulations, you hit the jackpot!"
                       if hit else f"\nThe drawn number was {drawn_number}, but your bet number was {bet_number}. Better luck next time!")
            print(message)
            
            # Step 4: Ask if the player wants to play again
            if not hit:
                response_options = False
                while not response_options:
                    play_response = input("\nDo you want to bet again?\nType yes or no: ")
                    if play_response == "yes":
                        print("\nAlright! Let's play again.\n")
                        response_options = True
                        reset_conditions()
                    elif play_response == "no":
                        print("\nThank you for playing!")
                        play_again = False
                        response_options = True
                    else:
                        print("\nPlease type yes or no.")
            else:
                play_again = False
        else:
            print("The bet number is not within the draw range.\n")
