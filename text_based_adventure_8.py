"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

This file will add functionality for the get function to allow us to collect
items and add them to our inventory

Tasks:

1) Step through the get function and make sure you understand how it works.
2) Add some extra items to your rooms that fit in with your theme.
3) Start to think about how the game will end. What are the win conditions?
   What does the player have top do with the items?
4) Test it to make sure it works
5) As a challenge you could try to write a drop function. This function will
   have to delete the item from your inventory and add it to the room dictionary
   for the corret room.

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
      return currentRoom
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

def get(inventory, currentRoom):
    if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    return inventory, currentRoom

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'item': 'hammer'
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

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    currentRoom = go(move, rooms, currentRoom)

  #if they type 'get' first
  if move[0] == 'get' :
    inventory, currentRoom = get(inventory, currentRoom)
