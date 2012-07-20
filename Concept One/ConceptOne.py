# Concept One for Rooms of Mystery
# This is still a work in progress - some things may escape me while programming or testing.

# Goal List: More rooms, monsters, player information, player saving and loading, add some secret rooms in + whatever 
# comes to mind.

# Importing some things
import time
import sys

# Firstly, I want a slow typed game name. Let's define that...suppose it could be used for anything where it's needed.
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

# Let's handle the items now, eh?
global oldGame, Bench, roomOneWording
# Starting amount of item(number)
oldGame = 0
bench = 0
roomOneWording = 0

# Just setting the inventory; empty to start.
invent = []

# Setting the items for finding.
items = ["Key One", "Key Two", "Key Three", "Key Four", "Hammer", "Bottle", "Boot"]

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
#|Room   |Room    |Room   |
#|10     |11      |12     |
#--------------------------
#|Room 7 | Room 8 | Room 9|
#|       |        |       |
#|---------------------------------
#|Room 4 | Room 5 | Room 6|Riddle |
#|       |        |       |Banish |
#|------------------------|Room   |
#|Room 1 | Room 2 | Room 3|--------
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
    raise SystemExit("\nSorry to see you go {0}, come back soon!".format(name))  
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
def system_error():
    print "\nGame error! Closing game! Inform iBoredom_ with documentation"
    print "to show what occurred. Post on GitHub or Broken Legion."
    raise SystemExit()
# END OF THE ALL AROUND THINGS (help, credits, commands, exit)

# Here we shall define the old man's game layout.
def old_man():
        print "\nYou begin to speak when the man interrupts you."
        print_slow("\nHello, {0}. Are you prepared to live or die?".format(name))
        print ""
        game = raw_input("Input: ").lower()
        if game == "yes":
            print ""
            print "\nThen answer my questions you must."
            print "What walks on four legs in the morning, two legs in the"
            print "evening, and three legs at night?"
            game2 = raw_input("Input: ").lower()
            if game2 == "man":
                print "\nCorrect. Next: A Person walked Parallel to a Legion of Elephants."
                game3 = raw_input("Input: ").lower()
                if game3 == "apple":
                    print "\nVery good."
                    print "Final question: What is as big as you are and yet does not weigh anything?"
                    game4 = raw_input("Input: ").lower()
                    if game4 == "your shadow":
                        print "\nCorrect. I shall move you to the next room and give you this key."
                        invent.append("Key Three")
                        oldGame = oldGame + 1 # The "flag" to prevent re-entry
                        room_eight()
                    else:
                        print "\nWrong answer! Good bye!"
                        print "A flash appears and you cannot see."
                        riddle_room()
                else:
                    print "\nWrong answer! Good bye!"
                    print "A flash appears and you cannot see."
                    riddle_room()
            else:
                print "\nWrong answer! Good bye!"
                print "A flash appears and you cannot see."
                riddle_room()
        else:
            print "\nThan leave my site you scum!"
            print "A flash appears and you cannot see."
            riddle_room()

# Beginning below is the room creations, in order from 1 - whatever is last.
# We keep only the rooms below here; games etc. should go above...try to not get unorganized to much.
# ROOM ONE - contains rooms to the EAST and NORTH. Exit behind you is locked for now.
def room_one():
    global roomOneWording
    if roomOneWording == 0:
        print "\nYou are standing in a room."
        room1 = raw_input("Input: ").lower()
        if room1 == "enter n":
            print "\nLEAVING ROOM."
            roomOneWording = roomOneWording + 1 # Change the text from the default to slightly confuse them? Maybe.
            room_four()
        elif room1 == "enter e":
            print "\nLEAVING ROOM"
            roomOneWording = roomOneWording + 1 # Change the text from the default to slightly confuse them? Maybe.
            room_two()
        elif room1 == "enter s":
            if "KeyOne" "KeyTwo" "KeyThree" "KeyFour" in invent:
                print "\nYou escape to your freedom! Congratulations, {0}!".format(name)
                print "Care to explore more, even if you have won?"
                game_won = raw_input("Yes or No: ").lower()
                if game_won == "yes":
                    start_menu()
                elif game_won == "no":
                    raise SystemExit("\nGood bye, {0}!".format(name))
            else:
                print "\nThis door is locked and has four key holes."
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
            exit()
        elif room1 == "room":
            print "\nThis is the room you started in."
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
        elif room1 == "i":
            print "\nYou currently have:"
            print invent
            room_one()
        else:
            print "\nInput error, please use a valid command."
            room_one()
    elif roomOneWording >= 1: # Changed text since they left and came back.
        print "\nYou enter the room."
        room1 = raw_input("Input: ")
        if room1 == "enter n":
            print "\nLEAVING ROOM."
            room_four()
        elif room1 == "enter e":
            print "\nLEAVING ROOM"
            room_two()
        elif room1 == "enter s":
            if "KeyOne" "KeyTwo" "KeyThree" "KeyFour" in invent:
                print "\nYou escape to your freedom! Congratulations, {0}!".format(name)
                print "Care to explore more, even if you have won?"
                game_won = raw_input("Yes or No: ").lower()
                if game_won == "yes":
                    start_menu()
                elif game_won == "no":
                    raise SystemExit("\nGood bye, {0}!".format(name))
            else:
                print "\nThis door is locked and has four key holes."
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
            exit()
        elif room1 == "room":
            print "\nThis is the room you started in."
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
        elif room1 == "i":
            print "\nYou currently have:"
            print invent
            room_one()
        else:
            print "\nInput error, please use a valid command."
            room_one()
# END ROOM ONE

# BEGIN ROOM TWO - Exits: North, East, West. Contains the hammer.
def room_two():
    print "\nYou enter the room."
    room2 = raw_input("Input: ").lower()
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
        if "Hammer" in invent:
            print "\nThe cabinet had a hammer in it. You've already taken it."
            room_two() 
        else:
            print "\nThe cabinet appears unlocked."
            room_two()
    elif room2 == "open cabinet":
        if "Hammer" in invent:
            print "\nYou've already opened the cabinet."
            room_two()
        else:
            print "\nYou open the cabinet and find a hammer!"
            invent.append("Hammer")
            room_two()
    elif room2 == "room":
        print "\nYou are in room 2."
        room_two()
    elif room2 == "commands":
        commands()
        room_two()
    elif room2 == "help":
        help()
        room_two()
    elif room2 == "exit":
        exit()
    elif room2 == "i":
        print "\nYou currently have:"
        print invent
        room_two()
    else:
        print "\nInput error, please use a valid command."
        room_two()
# END ROOM TWO

# BEGIN ROOM THREE - Exits: North, West. Contains the bench containing key two.
def room_three():
    global bench
    print "\nYou enter the room."
    room3 = raw_input("Input: ").lower()
    if room3 == "examine room":
        print "\nYou see a door to the west and north, and a stone bench."
        room_three()
    elif room3 == "enter w":
        print "\nLEAVING ROOM"
        room_two()
    elif room3 == "enter n":
        print "\nLEAVING ROOM"
        room_six()
    elif room3 == "examine bench":
        if bench == 0:
            print "\nThe bench seems hallow when you knock on it, perhaps something"
            print "could be used to break the stone?"
            room_three()
        elif bench >= 1:
            print "\nThe bench is broken."
            room_three()
    elif room3 == "break bench":
        if "Hammer" in invent and bench == 0: # This ensures only one breaking of the bench can happen by checking bench status.
            print "\nYou break the bench open, revealing a key!"
            bench = bench + 1 # Flag to make bench examine different as well as prevent them from "re-breaking".
            invent.append("Key Two")
            room_three()
        elif bench >= 1:
            print "\nThe bench is already broken."
            room_three()
        else:
            print "\nYou need something to perform this action."
            room_three()
    elif room3 == "room":
        print "\nThis is room three."
        room_three()
    elif room3 == "commands":
        commands()
        room_three()
    elif room3 == "help":
        help()
        room_three()
    elif room3 == "exit":
        exit()
    elif room3 == "i":
        print "\nYou currently have:"
        print invent
        room_three()
    else:
        print "\nInput error, please use a valid command."
        room_three()
# END ROOM THREE

# BEGIN ROOM FOUR - Exits: North, East, South. Contains key one.
def room_four():
    global oldGame
    print "\nYou enter the room."
    room4 = raw_input("Input: ").lower()
    if room4 == "examine room":
        if "Bottle" in invent:
            print "\nYou see exits to the north, east, and south."
            room_four()
        else:
            print "\nYou see exits to the north, east, and south, as well as"
            print "a bottle laying on the floor."
            room_four()
    elif room4 == "enter n":
        if oldGame == 0:
            print "\nLEAVING ROOM"
            room_seven()
        elif oldGame >= 1:
            print "\nThis door is locked now."
            room_four()
    elif room4 == "enter e":
        print "\nLEAVING ROOM"
        room_five()
    elif room4 == "enter s":
        print "\nLEAVING ROOM"
        room_one()
    elif room4 == "room":
        print "\nThis is room four."
        room_four()
    elif room4 == "examine bottle":
        if "KeyOne" in invent:
            print "\nThe bottle appears empty now."
            room_four()
        else:
            print "\nIt appears to have something in it."
            room_four()
    elif room4 == "take bottle":
        if "KeyOne" in invent:
            print "\nThe bottle is empty now."
            room_four()
        else:
            print "\nYou pick up the bottle and find a small key."
            invent.append("Key One")
            invent.append("Bottle")
            room_four()
    elif room4 == "help":
        help()
        room_four()
    elif room4 == "commands":
        commands()
        room_four()
    elif room4 == "exit":
        exit()
    elif room4 == "i":
        print "\nYou currently have:"
        print invent
        room_four()
    else:
        print "\nInput error, please use a valid command."
        room_four()
# END ROOM FOUR

# BEGIN ROOM FIVE - Exits in all directions. Contains key four.
def room_five():
    print "\nYou enter the room."
    room5 = raw_input("Input: ").lower()
    if room5 == "examine room":
        if "Boot" in invent:
            print "\nYou see an exit in every direction."
        else:
            print "\nYou see an exit in every direction, as well as a boot."
            room_five()
    elif room5 == "enter n":
        print "\nLEAVING ROOM"
        room_eight()
    elif room5 == "enter e":
        print "\nLEAVING ROOM"
        room_six()
    elif room5 == "enter s":
        print "\nLEAVING ROOM"
        room_two()
    elif room5 == "enter w":
        print "\nLEAVING ROOM"
        room_four()
    elif room5 == "examine boot":
        print "\nIt appears to be an old, leather boot."
        room_five()
    elif room5 == "take boot":
        if "KeyFour" in invent:
            print "\nThe boot is empty."
            room_five()
        else:
            print "\nYou take the nasty boot and see something within."
            print "You reach in and take a key from the boot."
            invent.append("Key Four")
            invent.append("Boot")
            room_five()
    elif room5 == "room":
        print "This is room five."
        room_five()
    elif room5 == "help":
        help()
        room_five()
    elif room5 == "commands":
        commands()
        room_five()
    elif room5 == "exit":
        exit()
    elif room5 == "i":
        print "\nYou currently have:"
        print invent
        room_five()
    else:
        print "\nInput error, please use a valid command."
        room_five()
# END ROOM FIVE

# START ROOM SIX - Exits: North, South, West.
def room_six():
    print "\nYou enter the room."
    room6 = raw_input("Input: ").lower()
    if room6 == "examine room":
        print "\nYou see exits to the north, west, and south. Nothing more."
        room_six()
    elif room6 == "enter n":
        print "\nLEAVING ROOM"
        room_nine()
    elif room6 == "enter w":
        print "\nLEAVING ROOM"
        room_five()
    elif room6 == "enter s":
        print "\nLEAVING ROOM"
        room_three()
    elif room6 == "room":
        print "\nThis is room six."
        room_six()
    elif room6 == "help":
        help()
        room_six()
    elif room6 == "commands":
        commands()
        room_six()
    elif room6 == "exit":
        exit()
    elif room6 == "i":
        print "\nYou currently have:"
        print invent
        room_six()
    else:
        print "\nInput error, please use a valid command."
        room_six()
# END ROOM SIX

# BEGIN ROOM SEVEN - let's actually add a mini-game here (winning: key three). Once completed, it's "flagged" to prevent players from reentering this room.
def room_seven():
    global oldGame
    print "\nYou enter the room, door disappearing behind you."
    room7 = raw_input("Input: ").lower()
    if room7 == "examine room":
        print "\nYou see no doors - just an old man standing before you."
        room_seven()
    elif room7 == "examine old man":
        print "\nHis face is covered, perhaps you could talk to him."
        room_seven()
    elif room7 == "enter s":
        print "\nThe door had disappeared"
        room_seven()
    elif room7 == "room":
        print "\nThis is room seven."
        room_seven()
    elif room7 == "talk to old man":
      old_man()
    elif room7 == "help":
        help()
        room_seven()
    elif room7 == "commands":
        commands()
        room_seven()
    elif room7 == "exit":
        exit()
    elif room7 == "i":
        print "\nYou currently have:"
        print invent
        room_seven()
    else:
        print "\nInput error, please use a valid command."
        room_seven()
# END ROOM SEVEN AND OLD MAN'S GAME

# BEGIN ROOM EIGHT - Exits: East, West, South
def room_eight():
    print "\nYou enter the room."
    room8 = raw_input("Input: ").lower()
    if room8 == "examine room":
        print "\nYou see a door to the east, west, and south, nothing more."
        room_eight()
    elif room8 == "enter e":
        print "\nLEAVING ROOM"
        room_nine()
    elif room8 == "enter w":
        print "\nThe door is locked, you'll have to enter somewhere else."
        room_eight()
    elif room8 == "enter s":
        print "\nLEAVING ROOM"
        room_five()
    elif room8 == "room":
        print "\nThis is room eight."
        room_eight()
    elif room8 == "help":
        help()
        room_eight()
    elif room8 == "commands":
        commands()
        room_eight()
    elif room8 == "exit":
        exit()
    elif room8 == "i":
        print "\nYou currently have:"
        print invent
        room_eight()
    else:
        print "\nInput error, please use a valid command."
        room_eight()
# END ROOM EIGHT

# BEGIN ROOM NINE - Box moving player to room one - may get more use later.
def room_nine():
    print "\nYou enter the room."
    room9 = raw_input("Input ").lower()
    if room9 == "examine room":
        print "\nYou see a door to the south and west, as well as a box."
        room_nine()
    elif room9 == "enter w":
        print "\nLEAVING ROOM"
        room_eight()
    elif room9 == "enter s":
        print "\nLEAVING ROOM"
        room_six()
    elif room9 == "examine box":
        print "\nIt appears to be a box made of wood. It could be opened."
        room_nine()
    elif room9 == "open box":
        print "\nYou open the box and are engulfed by darkness."
        room_one()
    elif room9 == "room":
        print "\nThis is room nine."
        room_nine()
    elif room9 == "help":
        help()
        room_nine()
    elif room9 == "commands":
        commands()
        room_nine()
    elif room9 == "exit":
        exit()
    elif room9 == "i":
        print "\nYou currently have:"
        print invent
        room_nine()
    else:
        print "\nInput error, please use a valid command."
        room_nine()
# END ROOM NINE

# BEGIN RIDDLE ROOM - incorrect answers and/or refusal to play the old man's game sends the player here.
def riddle_room():
    print "\nThe flash disappears, leaving you in a strange room."
    rroom = raw_input("Input: ")
    if rroom == "examine room":
        print "\nYou can only see the faint engravings someone made in the wall and the outline of a door."
        riddle_room()
    elif rroom == "examine engravings":
        print "\nthe riddle on the door holds the key to leaving this room..."
        print "...death to those who get it wrong"
        riddle_room()
    elif rroom == "examine door":
        print "\nYou see a riddle on the door."
        riddle_room()
    elif rroom == "examine riddle":
        print "\nIt is an insect, and the first part of its name is the name of another insect. What is it?"
        answer = "beetle"
        riddle = raw_input("Guess: ").lower() # Incorrect response means death. Increase to three tries?
        guesses = 0
        
        while riddle != answer and guesses < 2:
            print "\nThat is wrong, {0}.".format(name)
            print "Try again, perhaps? How many more do you get, aHahaha!"
            guesses += 1
            riddle = raw_input("Guess: ").lower()
            
        if riddle == answer:
            print "\nLeave this room, you shall."
            room_one()
        else: # Death to the player. Sad. Reloads the start menu upon key entry.
            print "\nYou hear a voice: good bye, {0}. Rest in peace.".format(name)
            print "\nThe room begins to fill with an oder of something foul."
            print "You have no way to escape."
            print "\nYou have died!"
            raw_input("Press any key to continue.")
            start_menu()
    elif rroom == "i":
        print "\nYou currently have:"
        print invent
        riddle_room()
    else:
        print "\nInput error, please use a valid command."
        riddle_room()
# END RIDDLE ROOM
# END ROOMS
    
# BEGIN START MENU
# I like having 'callable' start menus, so let's make one.
def start_menu():
    print "\nWelcome, {0}, please choose an option to begin.".format(name)
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
print "\nWelcome, {0}, please choose an option to begin.".format(name)
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