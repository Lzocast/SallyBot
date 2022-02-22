#!/usr/bin/env python3
# Simple interactive script for Python Practice
# This script is being continually iterated upon and at present only works as intended if you have the following:
    # 1. Sally version 2.1 or above
    # 2. The complimentary scripts game2.py, Weather.py & saytime.py in the SAME directory as Sally
    # 3. The python module 'requests' installed (install instructions in Weather.py)

# Eventual plan to have the D&D game less linear. Current attempts cause broken loops or crashes.

__version__: '3' # REV date 22/02/2022

from os import execl, execle, execlp, execv
import time
from datetime import datetime
import random
# Sys allows the appending of non-standard/selfmade modules from outside directory of current python file
# If you don't have the saytime module then comment out everything from here till the definition for rules and delete
# the call for the saytime_t().words() modules in the Main function
import sys
# Use the below example, altered to match where you have stored the saytime module:
        # ie: sys.path.append('D:\Python Course\Essentials\Chapter 2') 
# # Can be commented out if saytime.py is in same directory as Sally
# below imports all the classes/abilities of the below custom made module
from saytime import *

# To allow Sally to tell the user the weather in her area based on OpenWeather API JSON data.
from Weather import *

import game2
# D&D game text adventure game module. 



rules = [ 'Rock', 'Paper', 'Scissors' ]

# Function to define the simple game Sally plays with user
def go(ans):
    comp = random.choice(rules)
    if ans == comp:
        print(f"You chose {ans} and Sally chose {comp}")
        print("Sally: What the hell! How did that happen!? xD")
        time.sleep(4)
        return game("That was fun, we should do it again! ")
    elif ( ans == 'Rock' and comp == 'Paper' ):
        print(f"You chose {ans} and Sally chose {comp}")
        print("Sally: HA! I won!")
        time.sleep(4)
        return game("That was fun, we should do it again! ")
    elif ( ans == 'Paper' and comp == 'Rock' ):
        print(f"You chose {ans} and Sally chose {comp}")
        print("Sally: Nooooo! I lost :(")
        time.sleep(4)
        return game("That was fun, we should do it again! ")
    elif ( ans == 'Scissors' and comp == 'Paper' ):
        print(f"You chose {ans} and Sally chose {comp}")
        print("Sally: Noooo! I lost :(")
        time.sleep(4)
        return game("That was fun, we should do it again! ")
    elif ( ans == 'Paper' and comp == 'Scissors' ):
        print(f"You chose {ans} and Sally chose {comp}")
        print("Sally: Ha! I won!")
        time.sleep(4)
        return game("That was fun, we should do it again! ")
    elif ( ans == 'Rock' and comp == 'Scissors' ):
        print(f"You chose {ans} and Sally chose {comp}")
        print("Sally: Nooooo! I lost :(")
        time.sleep(4)
        return game("That was fun, we should do it again! ")
    elif ( ans == 'Scissors' and comp == 'Rock' ):
        print(f"You chose {ans} and Sally chose {comp}")
        print("Sally: HA! I won!")
        time.sleep(4)
        return game("That was fun, we should do it again! ")
    else:
        print("Sally: Hmm, don't think that was an option. But we can try again next time")
        time.sleep(3)
        return game("I'll go over the rules again. ")

def print_list(o):
    for i in o: 
        print(i, end =' ', flush = True)
    print()

# Function to define the Sally's interest in games and play one if user is amiable.    
def game(question):
    prompt = f'{question} Would you like to play a simple game? (y/n):'
    #Takes the answer from the above question and lowercases it and strips out
    # everything except the y or the n to make if statement easier to code.
    answer = input(prompt).strip('es').strip('o').lower()
    if answer not in ['y', 'n']:
        print(f'Sally: {answer} is not an option, lets start again')
        return game(question)
    if answer == 'y':
        print("Sally: Splendid!")
        time.sleep(2)
        print('Sally: This game is simple. You just pick one of the three choices below:')
        print()
        print_list(f'\t{rules}')
        print()
        time.sleep(3)
        print("Sally: Got it? I'll count to three then we both type ok?")
        time.sleep(3)
        print('One..')
        time.sleep(2)
        print('Two..')
        time.sleep(2)
        choice = input('Three! ').capitalize()
        go(choice)
    else:
        options = input("Sally: Oh, that is a shame.... OH! Unless you'd like to try something more interesting? \nI run a mean 'Choose your own D&D'? y/n? ")
        if options == 'y':
            game2.main()
        else:
            return
            


    

# Main function to define how to ask questions and how to end the conversation
def main():
    name = input("Sally: Hello there, what is your name? ")
    print("Sally: Nice to meet you,", name)
    game("Sally: I'm so happy I made a new friend!")
    time.sleep(5)
    print ('Sally: Oops! I need to go, it\'s ' + saytime_t().words() + ' ,but I hope we can talk again soon <3')
    time.sleep(3)
    print('Sally: I should check the weather before I go though... let\'s see...\n')
    time.sleep(3)
    Weather()
    print()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("\n>>> [Sally] logged off at:", current_time,"<<<\n")

if __name__ == "__main__":
    main()