"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

You may have noticed that in the previous version of the programme the
currentRoom variable was not being updated as you moved around. This is because
the value is only being changed inside the go function and not globally. We will
corrrect this.

This file will:

1) Return values out of functions to be changed globally.

Tasks:

1) Make sure you understand how the variables are passed into and returned from
the functions.
2) Test it to make sure it works. You should see the current location updated as
you move around.
3) Start to think about what the get funcion needs to do. You could sketch this
out on paper as a flow diagram or use pseudo code.
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

def showStatus(currentRoom):
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
      return currentRoom

    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
        return currentRoom

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

  showStatus(currentRoom)
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
    currentRoom = go(move, rooms, currentRoom)

  #if they type 'get' first
  if move[0] == 'get' :
    get()
