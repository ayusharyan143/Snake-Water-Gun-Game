'''
    1 for snake 
    -1 for water 
    0 for gun


'''




import random 



# Choices dictionary
choices = { 1:"Snake" , -1:"Water" , 0:"Gun" }
youDict = { "s": 1, "w": -1, "g": 0, "S": 1, "W": -1, "G": 0 }




# Function to get the computer's choice
def get_computer_choice():
    return random.choice([1 , -1 , 0])




# Function to determine the winner
def determine_winner( computer , you ):
    if( computer == you ):
        return "It's a tie!"
    elif( computer == 1 and you -1 ) or ( computer == -1 and you == 0 ) or ( computer == 0 and you == 1 ):
        return "You Lose!"
    else:
        return "You Win!"



# Main game logic
def play_game():
    
    computer_choice = get_computer_choice()
    you_choice_input = input("Enter your choice (s for Snake, w for Water, g for Gun): ")

    if ( you_choice_input not in youDict ):
        print("Invalid choice! Please choose 's', 'w', or 'g' ")
        return 
    
    you_choice = youDict[ you_choice_input ]
    
    print(f"Computer chose: {choices[computer_choice]} ")
    print(f"You chose: {choices[you_choice]}")
    
    result = determine_winner( computer_choice , you_choice )

    print(result)

    
# Start the game
play_game()