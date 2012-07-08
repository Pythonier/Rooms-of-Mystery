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

# Well, I can try to keep these semi-organized, but no promises.
# BEGIN ALL AROUND COMMANDS
# Let's define the exit, credits, help all within one section.
def exit():
    raise SystemExit("\nThanks for playing, please play again!")
def help():
    print "\nYou play this game by typing what you wish to do."
    print "The game involves you trying to escape, but be warned"
    print "monsters and surprises await! Type commands at any time to"
    print "see what commands can be used!"
def credits():
    print "\nRooms of Mystery by iBoredom_"
    print "Game Concept by iBoredom_"
    print "Game written and thought of by iBoredom_"
    print "Thanks to anyone who helped me along the way, from ideas"
    print "to grammar and small code mistakes!"
# END OF THE ALL AROUND COMMANDS (help, commands, exit)

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
        game_begin()
    elif start == "2":
        exit()
    elif start == "3":
        credits()
        start_menu()
    elif start == "4":
        help()
        start_menu()
# END OF START MENU

# Let's create the opening sequence - use the print_slow for title.
# Also includes the basic starting options.
# Final Note: Keeping this at the bottom of the code so the functions can be called.
print "\nWaking up inside a place you don't remember - always fun."
print "But this place seems different, darker, mysterious."
print "You're in for a long night. Welcome to..."
print_slow("\nROOMS OF MYSTERY") # slow printing text thanks to print_slow
print_slow("\nA terminal text adventure by: iBoredom_")
print ""
print "\nPlayer, please choose an option to begin." # this line break appears useless, so we created a blank print
print "1. Play 'Rooms of Mystery'"
print "2. Exit Game"
print "3. View Game Credits"
print "4. View Game Help"
start = raw_input("> ").lower()
if start == "1":
    game_begin()
elif start == "2":
    exit()
elif start == "3":
    credits()
    start_menu() # call a simplified version, skip the beginning printing
elif start == "4":
    help()
    start_menu()