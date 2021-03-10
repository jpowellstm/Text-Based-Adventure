"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

This file will:

1) Start adding functionality into the go function.

Tasks:

1) Step through the code in the go function and make sure you understand what is
going on.
2) Make sure you pass the move, rooms and currentRoom variables into the
functions.
3) Test it to make sure it works. You should now be able to move betwen rooms.
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

def go(move, rooms, currentRoom):
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

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

  #if they type 'go' first
  if move[0] == 'go':
    go(move, rooms, currentRoom)

  #if they type 'get' first
  if move[0] == 'get' :
    get()

