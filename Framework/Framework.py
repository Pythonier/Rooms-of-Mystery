# Framework for Rooms of Mystery
# Remember, this will be buggy, glitchy, and things may not work right - oh well, Framework wasn't designed to be perfect.

# Importing some things
import time
import sys

# Firstly, I want a slow typed game name. Let's define that...suppose it could be used for anything where it's needed.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)
    
# BEGIN TITLE SEQUENCE
# Let's create the opening sequence - use the print_slow for title.
# We will also gather the player's name here.
print "\nWaking up inside a place you don't remember - always fun."
print "But this place seems different, darker, mysterious."
print "You're in for a long night. Welcome to..."
print_slow("\nROOMS OF MYSTERY") # slow printing text thanks to print_slow
print_slow("\nA terminal text adventure by: iBoredom_")
print "" # Line breaks after calling print_slow don't work, so we need this empty print.
name = raw_input("\nWhat is your name, dear adventurer: ").capitalize()
# END TITLE SEQUENCE

# START ROOM LAYOUT EXAMPLE
# Note: Framework is 9 rooms, final may be up to or more than 24.
#--------------------------
#|Room 7 | Room 8 | Room 9|
#|       |        |       |
#|-------------------------
#|Room 4 | Room 5 | Room 6|
#|       |        |       |
#|-------------------------
#|Room 1 | Room 2 | Room 3|
#|       |        |       |
#|-------------------------
#|Final  |
#|Room   |
#|-locked|
#|-------|
# END ROOM LAYOUT EXAMPLE

# Well, I can try to keep these semi-organized, but no promises.
# BEGIN ALL AROUND THINGS (help, credits, commands, exit,)
# Let's define the exit, credits, help all within one section.
def exit():
    raise SystemExit("\nThanks for playing, {0}, please play again!".format(name))
def help():
    print "\nYou play this game by typing what you wish to do."
    print "The game involves you trying to escape, but be warned"
    print "monsters and surprises await! Type commands at any time to"
    print "see what commands can be used!"
def credits():
    print "\n- Rooms of Mystery by iBoredom_"
    print "- Game Concept by iBoredom_"
    print "- Game written and thought of by iBoredom_"
    print "- Thanks to anyone who helped me along the way, from ideas"
    print "- to grammar and small code mistakes!"
def commands():
    print "\nThe basic commands consist of the following:"
    print "enter (n, s, e, w), take (object), examine (thing), room (tells you room number)"
    print "help, exit (ends game)"
    print "Some rooms may have hidden commands which can be found"
    print "by examining the rooms and/or objects within."
# END OF THE ALL AROUND THINGS (help, credits, commands, exit)

# Beginning below is the room creations, in order from 1 - whatever is last.
# ROOM ONE - contains rooms to the EAST and NORTH. Exit behind you is locked for now.
def room_one():
    print "\nYou are standing in a room."
    room1 = raw_input("Input: ")
    if room1 == "enter n":
        print "\nLEAVING ROOM."
        room_four()
    elif room1 == "enter e":
        print "\nLEAVING ROOM"
        room_two()
    elif room1 == "enter s":
        print "This door is locked."
        room_one()
    elif room1 == "examine room":
        print "\nYou see a door to the north, east, and south, as well as a table."
        room_one()
    elif room1 == "help":
        help()
        room_one()
    elif room1 == "commands":
        commands()
        room_one()
    elif room1 == "exit":
        quit()
    elif room1 == "room":
        print "This is the room you started in."
        room_one()
    elif room1 == "examine table":
        print "\nYou see a note on the table that you could read."
        room_one()
    elif room1 == "read note":
        print "\nYou pick up the note and read it."
        print "\n\tWelcome to my game, {0}.".format(name)
        print "\tFind the exit to escape!"
        print "\tForever watching,"
        print "\n\t\t[Evil Name Here]"
        room_one()
    else:
        print "\nInput error, please use a valid command."
        room_one()
# END ROOM ONE

# BEGIN ROOM TWO
def room_two():
    print "\nYou enter the room."
    room2 = raw_input("Input: ")
    if room2 == "examine room":
        print "\nThe room has exits to the west, north, and east. You also see"
        print "a cabinet."
        room_two()
    elif room2 == "enter n":
        print "\nLEAVING ROOM"
        room_five()
    elif room2 == "enter w":
        print "\nLEAVING ROOM"
        room_one()
    elif room2 == "enter e":
        print "\nLEAVING ROOM"
        room_three()
    elif room2 == "examine cabinet":
        print "\nThe cabinet appears unlocked."
        room_two()
    elif room2 == "open cabinet":
        print "\nThe cabinent is empty."
        room_two()
    elif room2 == "room":
        print "\nYou are in room 2."
    elif room2 == "help":
        help()
    elif room2 == "commands":
        commands()
    elif room2 == "quit":
        quit()
    else:
        print "Input error, please use a valid command."
        room_two()
# END ROOM TWO
    
    
#BEGIN START MENU
# I like having callable start menus, so let's make one.
def start_menu():
    print "\nPlayer, please choose an option to begin." # this line break appears useless, so we created a blank print
    print "1. Play 'Rooms of Mystery'"
    print "2. Exit Game"
    print "3. View Game Credits"
    print "4. View Game Help"
    start = raw_input("> ").lower()
    if start == "1":
        room_one()
    elif start == "2":
        exit()
    elif start == "3":
        credits()
        start_menu()
    elif start == "4":
        help()
        start_menu()
    else:
        print "\nInput error, please choose a valid option."
        start_menu()
# END OF START MENU

# BEGIN OPENING CHOICES
# This will display after the player inputs their name.
# Also includes the basic starting options.
# Final Note: Keeping this at the bottom of the code so the functions can be called.
print "\nWelcome, {0}, please choose an option to begin.".format(name) # this line break appears useless, so we created a blank print
print "1. Play 'Rooms of Mystery'"
print "2. Exit Game"
print "3. View Game Credits"
print "4. View Game Help"
start = raw_input("> ").lower()
if start == "1":
    room_one()
elif start == "2":
    exit()
elif start == "3":
    credits()
    start_menu() # call a simplified version, skip the beginning printing
elif start == "4":
    help()
    start_menu()
else:
    print "\nInput error, please choose a valid option."
    start_menu()
# END OPENING CHOICES