# Importing all the needed from all other files.
# First importing the logo
from art import logo
# Importing the vs symbol
from art import vs
# Importing all the followers data
from game_data import data
# Importing random pick function from random module
from random import randint


# Creating a function with return of random number from 0 to 49. So that it would be easy to pick something from the
# game data.
def random_number():
    number = randint(0, 49)
    return number


# Creating a boolean variable for running a while loop.
end_of_game = False
# Creating a variable to keep track of how many times the while loop is running.
times_running = 0
# Creating a variable to store the previous high follower data.
previous = {}

# Starting the game.
while not end_of_game:
    # Adding +1 to the rimes_running variable every time the loop runs.
    times_running += 1
    score = times_running - 1

    # If it the first time then picking the random datta by ourselves but if it is second time or more then storing the
    # previous high in this.
    if times_running == 1:
        a = data[random_number()]
    else:
        a = previous
    # Creating a second data all the time.
    b = data[random_number()]

    # Printing and showing the user both of their names, a small description and the country from which they are from.
    # Also printing some logos. Also printing the score
    print(logo)
    print(f"You score is {score}")
    print(f"Compare 1 : {a['name']}, a {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Compare 2 : {b['name']}, a {b['description']}, from {b['country']}.")

    # Making the user to make a guess.
    guess = int(input("Who has more followers, 1 or 2?: "))

    # If the user made the guess correct then just giving them a feedback, or else changing the boolean variable so that
    # the loop ends.
    if a["follower_count"] > b["follower_count"] and guess == 1:
        print("You got it right. ")
    elif a["follower_count"] < b["follower_count"] and guess == 1:
        print("You got it wrong.")
        end_of_game = True
    elif a["follower_count"] > b["follower_count"] and guess == 2:
        print("You got it wrong.")
        end_of_game = True
    elif a["follower_count"] < b["follower_count"] and guess == 2:
        print("You got it right.")
    else:
        print("Oops, you made a typo.")

    # Setting the highest one with follower to previous variable so that when the loop runs again this can be stored as
    # first data.
    if a["follower_count"] > b["follower_count"]:
        previous = a
    if a["follower_count"] < b["follower_count"]:
        previous = b
