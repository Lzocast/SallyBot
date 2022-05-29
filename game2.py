#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Added coded in main(),and create a function to ask for your name and return it.
#

import time
import SallyV3

# --- Treasure ---
treasure_chest = ["3 diamonds", "10 gold pieces", "4 silver pieces", "a gleaming sword"]


# --- ACTIONS ---
def you_died(why):
    """
    In: Passing in the string showing player how they dies
    Result:
    Prints reason why they player died.
    Programme exits without error.
    """
    print("Dm_Sally: {}. Good job!".format(why))

    # This exits the program entirely.


# --- END ACTIONS---

# --- CHARACTERS---
def guard():
    """
    Encountering the guard, the player chooses to attack, check or sneak.
    - attack: player dies and it is game over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    - leave: player is returned to room enter state
    """
    # Actions on the guard
    actions_dict = {
        "check": (
            "\nDM_Sally: You see the guard is still sleeping; a faint wisp of fresh air"
            " caresses your face, coming from the door on the right of him. What are you"
            " waiting for?\n"
        ),
        "sneak": (
            "\nDM_Sally: You approach the guard, he's still sleeping. Reaching for the door,"
            " you open it slowly... The guard shifts... and slip out.\n"
        ),
        "attack": (
            "\nDM_Sally: Steeling yourself you move swiftly towards the sleeping guard, still"
            " trying to decide if you mean to land a killing blow or just knock him out with"
            " the hilt of your sword. Unfortunately things don't go as planned.\n"
        ),
        "leave": "\nDM_Sally: Hmm, perhaps it's safer to just leave him be for now",
    }

    # While loop
    while True:
        action = input("DM_Sally: What do you do? [attack | check | sneak]? >").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print(
                    "DM_Sally: You just slipped through the door before the guard realised it."
                )
                time.sleep(2)
                print("DM_Sally: You are now outside, home free! Huzzah!\n")
                return
            elif action == "attack":
                you_died(
                    "As you move forward to strike, your foot presses down on a loose board"
                    " with a loud 'creeeeEEEEaak'.  Woken by the noise the Guard reaches for"
                    " his dagger, and as you scramble for your sword pain blossoms in your"
                    " chest and everything goes grey... and dark... You just died.\n<GAME OVER>"
                )


# --- END CHARACTERS---

# --- ROOMS ---
def blue_door_room(t):
    """
    The player finds a treasure chest, options to investigate the treasure chest
    or guard.
    If player chooses - Treasure chest: show its contents; option to take
    treasure or ignore it (proceeds to guard) - Guard: After checking treasure
    chest, ignoring treasure chest to check guard, it calls guard() function
    """
    # NOTE So our treasure_chest list contains 4 items RETURN TREASURE_CHEST
    # HERE IF CODE FUCKED

    print(t)

    # Ask player what to do.
    action = input("What do you do? > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("DM_Sally: Oooh, treasure!")

        print("DM_Sally: Open it? Press '1'")
        time.sleep(3)
        print("DM_Sally: Leave it alone. Press '2'")
        choice = input("> ")

        if choice == "1":
            print("DM_Sally: Let's see what's in here... /grins")
            time.sleep(3)
            print(
                "DM_Sally: The chest creaks open... the guard stirs... snorts... and resumes"
                " his rest. That's one heavy sleeper!"
            )
            time.sleep(4)
            print("DM_Sally: You find the following items: ")

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure.upper())

            time.sleep(7)

            # So much treasure, what to do? Take it or leave it.
            print("\nDM_Sally: What do you want to do?\n")
            # Get number of items in treasure chest with len))
            num_items_in_chest = len(treasure_chest)

            time.sleep(3)

            print(f"DM_Sally: To take all {num_items_in_chest} treasure items, press '1'")
            print("DM_Sally: To leave it for now, press '2'")

            treasure_choice = input("Your Decision > ")
            if treasure_choice == "1":
                treasure_chest.remove("a gleaming sword")
                print(
                    "\tDM_Sally: You take the gleaming sword from the treasure chest. It does"
                    " looks exceedingly shiney."
                )
                time.sleep(3)
                print(
                    "\tDM_Sally: Woohoo! Bounty and a shiney new sword. You discard your"
                    " current, much crapier, sword in the chest."
                )

                temp_treasure_list = treasure_chest[:]
                treasure_contents = ", ".join(treasure_chest)
                print(f"\tYou also receive {treasure_contents}.")

                # Removing all the rest of the items in the treasure chest
                for treasure in temp_treasure_list:
                    # Use list remove() function to remove each item in the chest.
                    treasure_chest.remove(treasure)

                # Add the old sword in place of the new sword
                treasure_chest.append("crappy sword")
                print(
                    "\nDM_Sally: You close the lid of the chest containing the"
                    f" {treasure_chest} for the next adventurer. /grins\n"
                )
                time.sleep(5)
                print(
                    "DM_Sally: Now onward to get past this sleeping guard and the door to"
                    " freedom... "
                )
            elif treasure_choice == "2":
                print(
                    "DM_Sally: Treasure is all well and good, but getting out of here would be"
                    " better"
                )
        elif choice == "2":
            print("DM_Sally: Whatever is in there can wait, you need to escape")
    elif action.lower() in ["guard", "right"]:
        print(
            "DM_Sally: Good thinking, you should probably make sure you know what is up with"
            " that Guard."
        )
    else:
        print(
            "DM_Sally: Well, not sure what you picked there, soooooooo let's poke the guard cos"
            " it's fun!"
        )
    guard()


def red_door_room(t):
    """
    The red door rooom contains a red dragon.
    If a player types "flee" as an answer, player returns to the room with two doors,
    otherwise the player dies.
    """
    print(t)
    time.sleep(9)
    print(
        "DM_Sally: It stares at you through one narrowed eye for a moment.... and you could"
        " swear it seems to grin as a ravenous understanding fills that gaze."
    )
    time.sleep(6)
    print("DM_Sally: Do you flee for your life or stay and try to face the monster?")

    next_move = input("Your Decision: [flee | stay] > ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure(
            "\nDM_Sally: Reaching slowly behind you, you fumble for the door handle. Wincing as"
            " the hot metal sears your palm, you back through the opening and slam the door"
            " closed as soon as you are through. Heart pounding you reconsider your choices in"
            " life and decide to pretend that never happened."
        )

        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
    you_died(
        "You're taking on a dragon with only a sword... Well, it eats you.... But at least you"
        " gave it indigestion!"
    )


# --- END ROOMS---


def end_adventure():
    print("\n\tThe end\n")
    print(f"DM_Sally: Thanks for playing, {player_name.upper()}\n")
    exit


def get_player_name():
    """
    Gets players name, may or may not be renamed depending on player's choice.
    Returns: Player name back (altered or unaltered)
    """
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    name = input("DM_Sally: Ahem. What's your name Adventurer? > ")

    time.sleep(3)

    # This is just an alternative name that the game wants to call the player
    alt_name = "Lord Fluffington"
    answer = input(f"DM_Sally: Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print(f"DM_Sally: You're fun, {name.upper()}! Let's begin our adventure!")

    elif answer.lower() in ["n", "no"]:
        print(f"DM_Sally: Ok, picky. {name.upper()} it is. Let's get started :)")
    else:
        print("DM_Sally: Well I like it, so {alt_name.upper()} it is!")
        name = alt_name

    # Now notice that we are returning the variable called name.  In main(), it
    # doesn't know what the variable "name" is, as it only exists in
    # get_player_name() function.  This is why indentation is important,
    # variables declared in this block only exists in that block
    return name


def start_adventure(t):
    """
    This function starts the adventure by allowing two options for
    players to choose from: red or blue door
    Chosen option will print out the door chosen.
    """
    print(t)

    time.sleep(4)

    door_picked = input(
        "DM_Sally: As you ease yourself up on aching muscles, brushing away bits of damp hay"
        " from your clothes, do you pick the red door or blue door?\nYour Decision [red |"
        " blue] > "
    )

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        red_door_room(
            "\nDM_Sally: The door grinds open on stiffened hinges... and there you see a great"
            " red dragon. Towering and magnificent, flames tickle the edge of nostrils the size"
            " of your head as it breathes. Teeth as long as your arm poke out from its maw..."
            " and as if sensing the stilling of your heart the beast swivels its scaly head to"
            " regard you."
        )
    elif door_picked == "blue":
        blue_door_room(
            "\nDM_Sally: Opening the door slowly you see a room with a wooden treasure chest on"
            " the left, and a sleeping guard sat on a simple stool on the right in front of the"
            " a plain iron door"
        )
    else:
        print(
            "DM_Sally: Sorry, it's either 'red' or 'blue' as the answer. Look, let's start over"
        )
        return start_adventure(
            "You've come to in bare stone room, on a pile of stinking hay. To your left is a"
            " red door, to your right a blue door"
        )


def main():
    print("\n===================================================")

    print("\t    Welcome, Brave Soul, to...")

    title = ["Sally's D&D Adventure!"]

    def print_list(o):
        for i in o:
            print(i, end=" ", flush=True)
        print()

    print_list(f"{title}")

    print("===================================================\n")

    """
    Gets the players name by calling get_player_name() before starting the adventure.
    """
    global player_name
    player_name = get_player_name()

    time.sleep(3)

    start_adventure(
        "\nDM_Sally: Your mind is fuzzy and your breathing raspy as you peel open dry eyes. In"
        " the sooty torch light you can make out four barren stone walls and facing each other"
        " on opposite sides of the room, two doors.  To your left is a red door, the air on"
        " that side of the room feels warm and sharp...  To your right you see a blue door,"
        " from under which skirts a cool, if musty breeze.\n"
    )

    end_adventure()


if __name__ == "__main__":
    main()

    
