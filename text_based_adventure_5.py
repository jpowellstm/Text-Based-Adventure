"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

This file will:

1) Refactor to move code for go and get into functions. This will make it easier
to add code in the future.

Tasks:

1) Add any extra functions for commands extra commands you made.
2) Make any modifications to fit your theme.
3) Test it to make sure it works. You should be able to do the same as you could
before.
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

def go():
    print('this is a place holder for go')

def get():
    print('this is a place holder for get')

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

while True:

  showStatus()

  """
  get the player's next 'move'
  .lower() makes it all lower case
  .split() breaks it up into an list array
  eg typing 'go east' would give the list: ['go','east']
  move[0] then gets the first item from the list, e.g. 'go'
  move[1] gets the second item from the list, e.g. 'east'
  """

  move = ''
  while move == '':
    move = input('>')

    move = move.lower().split()

    if move[0] == 'go':
        go()

    if move[0] == 'get' :
        get()

