# TODO: From a text file read in the text introduction of your game and print it to the console.
story_file = open('D:\\Documents\\School\\Spring 2022\\WEB 3200 - Dynamic Languages for Web Development\\Assignment 4 - TextAdventure\\game_instructions.txt', 'r')
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())
print(story_file.readline())

# TODO: Setup a dictionary with several key value pairs. It should contain an inventory list and the initial location. Call the dictionary `player`.
# TODO: Set up a dictionary of rooms each room having a description, a list of items and a dictionary of exits. Add 5 rooms. 

# TODO: Setup on infinite loop.

    # TODO: Create a variable and set it equal to the initial room stored in the `player` dictionary.
    # TODO: Create a variable to store the command that is input by the user. Allow for commands like `take sword`
    #       **Hint: `split()` and store the different parts in their own variables.**
    # TODO: Create four `if` statements
    # TODO: One that checks verbs and exits.
    #       Make sure you check if the player can go in the direction that the have asked for.
    #       This is where you list all of the items in the room.
    # TODO: One that allows the user to print the current inventory.
    # TODO: One that allows the user to quit.
    # TODO: One that allows the player to pick up single items and odd them to the inventory of the `player`.
    #       Also allow the user to add all items in the room to the inventory.

# Required Additions:
# TODO: In one room add a monster and have the player fight the monster (add an attack verb). Store the monster stats in a dictionary.
# TODO: In one room have the player talk with another character save the dialog.
# Create a map verb that prints a map of the dungeon.

#***may have to Run command 'pip install pandas' first then run game***
import pandas as pd

currloc_list = [["Adventurer", "Foyer", ""]]
curr_dict = pd.DataFrame(currloc_list, columns =['name', 'current_room', 'inventory'])

roominvent_list = [[1, "Foyer", "Rope"], [2, "Parlor", "Sword"], [3, "Kitchen", "Knife"], [4, "Library", "Spear"], [5, "Pantry", "Gun"]]
roominvent_dict = pd.DataFrame(roominvent_list, columns = ['roomno', 'rooms', 'items'])

def command():
  command = input("Enter a command like 'enter [room name]', 'inventory', 'take all items', 'take [item]', 'items', 'conversation', 'map', 'quit' : ")

def ghost():
  print("Hello, Im a ghost in the library. I am lonely. I like conversation. If you really don't want to converse type 'stop'")
  print("Ghost: Talk to me")
  ghost_talk = input('Adventurer: ')
  if ghost_talk == 'stop':
    print("You are currently in the library")
  elif ghost_talk == 'Hello Ghost!!!!!!': #have to type Hello Ghost! for it to go through
    print("Ghost: That's interesting talk to me some more")
    inp = input('Adventurer: ')
    if inp != 'stop':
      ghost_command1=input('Type "stop" to end conversation with Ghost: ')
    elif inp == 'stop':
      return

def monster():

  monster_command = input("Watch out! A monster is attacking you! To slay him you must hit and also hypnotize him (Use the commands 'karate chop' or 'hypnotize'):")

  if monster_command == 'karate chop':

    print('Good job, you have injured the monster. His health is now 0')

    monst = input("You are hurting the monster but you haven't slayed him. To slay him you must hit and also hypnotize him (Use the commands 'karate chop' or 'hypnotize'):")

    if monst == 'hypnotize':

      print("Good job, you have driven the monster crazy. His sanity is now 0")

      print("There is a monster in this room but you slayed it")

      

def map():

  print("-----------------------------------------------------------")

  print("|                       Foyer                             |")

  print("|                                                         |")

  print("------     --------------------------------     -----------")

  print("|        Parlor          |         Library w/ghost        |")

  print("|                        |                                |")

  print("------     --------------------------------     -----------")

  print("|                     Kitchen                             |")

  print("|                                                         |")

  print("------     ------------------------------------------------")

  print("|   Pantry w/monster    |")

  print("|                       |")

  print("-------------------------")

def item_list():

  if curr_dict.current_room[0] == 'Foyer':

    print('Rope')

  elif curr_dict.current_room[0] == 'Parlor':

    print('Sword')

  elif curr_dict.current_room[0] == 'Library':

    print('Spear')

  elif curr_dict.current_room[0] == 'Kitchen':

    print('Knife')

  elif curr_dict.current_room[0] == 'Pantry':

    print('Gun')

for i in range(1000):

  command = input("Enter a command like 'enter [room name]', 'inventory', 'take all items', 'take [item]', 'items', 'conversation', 'map', 'quit' : ")

  if command == 'enter parlor':

    if (curr_dict.current_room[0] == 'Foyer' or curr_dict.current_room[0] == 'Kitchen'):

      print("ok you have moved to: parlor")
      print("")
      print("You are currently in the parlor")

      curr_dict.loc[curr_dict['name'] == "Adventurer", 'current_room'] = 'Parlor'

    else:

      print("sorry cant move there")
      print("")
      print("You are currently in the foyer")

  elif command == 'enter library':

    if (curr_dict.current_room[0] == 'Foyer' or curr_dict.current_room[0] == 'Kitchen'):

      print("ok you have moved to: library")
      print("")
      print("You are currently in the library")

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'current_room'] = 'Library'

      ghost()

      print("You are currently in the library")   

    else:

      print("Sorry cant move there")
      print("")
      print("You are currently in the library")

  elif command == 'enter kitchen':

    if (curr_dict.current_room[0] == 'Parlor' or curr_dict.current_room[0] == 'Library' or curr_dict.current_room[0] == 'Pantry'):

      print("ok you have moved to: kitchen")
      print("")
      print("You are currently in the kitchen")

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'current_room'] = 'Kitchen'       

    else:

      print("Sorry cant move there")
      print("")
      print("You are currently in the kitchen")

  elif command == 'enter pantry':

    if (curr_dict.current_room[0] == 'Kitchen'):

      print("ok you have moved to: pantry")
      print("")
      print("You are currently in the pantry")

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'current_room'] = 'Pantry'

      monster()

      print("You are currently in the pantry")    

    else:

      print("Sorry cant move there")
      print("")
      print("You are currently in the foyer")

  elif command == 'enter foyer':

    if (curr_dict.current_room[0] == 'Parlor' or curr_dict.current_room[0] == 'Library'):

      print("ok you have moved to: foyer")
      print("")
      print("You are currently in the foyer")

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'current_room'] = 'Foyer'       

    else:

      print("Sorry cant move there")
      print("")
      print("You are currently in the foyer")

  elif command == 'map':

    map()

  

  elif command == 'inventory':

    print(f"Your inventory:[{curr_dict.inventory[0]}]")

  elif command == 'conversation':

    print("Here is the conversation you had with the ghost:")

    print("Ghost: Talk to me")

    print("Adventurer: Hello Ghost!!!!!!")

    print("Ghost: That's interesting talk to me some more")

    print("Adventurer: I bet your name is Casper!!!!")

  elif command == 'items':

    item_list()

  elif command == 'take all items':

    if curr_dict.current_room[0] == 'Foyer':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + 'Rope '
      print("Ok, you have added [Rope] to your inventory")
      print("")
      print("You are currently in the foyer")

    elif curr_dict.current_room[0] == 'Library':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + 'Spear '
      print("Ok, you have added [Spear] to your inventory")
      print("")
      print("You are currently in the library")

    elif curr_dict.current_room[0] == 'Kitchen':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + 'Knife '
      print("Ok, you have added [Knife] to your inventory")
      print("")
      print("You are currently in the kitchen")

    elif curr_dict.current_room[0] == 'Pantry':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + 'Gun '
      print("Ok, you have added [Gun] to your inventory")
      print("")
      print("You are currently in the pantry")

    elif curr_dict.current_room[0] == 'Parlor':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + 'Sword ' 
      print("Ok, you have added [Sword] to your inventory") 
      print("")
      print("You are currently in the parlor") 

  

  elif command == 'take gun':

    if curr_dict.current_room[0] == 'Pantry':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + ', Gun'

    else:

      print('No such item in the room')

  elif command == 'take spear':

    if curr_dict.current_room[0] == 'Library':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + ', Spear'

    else:

      print('No such item in the room')

  elif command == 'take knife':

    if curr_dict.current_room[0] == 'Kitchen':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + ', Knife'

    else:

      print('No such item in the room')

  elif command == 'take rope':

    if curr_dict.current_room[0] == 'Foyer':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + ', Rope'

    else:

      print('No such item in the room')

  elif command == 'take Sword':

    if curr_dict.current_room[0] == 'Parlor':

      curr_dict.loc[curr_dict['name'] == 'Adventurer', 'inventory'] = curr_dict.inventory[0] + ', Sword'

    else:

      print('No such item in the room')

  elif command == 'quit':

    print('Your adventure has ended!')

    break