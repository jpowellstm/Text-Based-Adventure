"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

This file will:

1) Add a function to print out details of where the player is, what items they
have and what is available in the room.
2) Call the function to test it.

Tasks:

1) Modify the showStatus function to fit your theme.
2) Test it to make sure it works. You make sure that any items available are
printed.
"""

def showInstructions():
  """print a main menu and the commands
  """
  print("""
  RPG Game
  ========
  Commands:
  go [direction]
  get [item]

	""")

def showStatus():
  """print out information about:
  where the player is,
  what the player has in their inventory,
  what items are available in the room.
  """
  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Inventory : ' + str(inventory))

  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])

  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen'
                },

            'Kitchen' : {
                  'north' : 'Hall'
                }

         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()
showStatus()
