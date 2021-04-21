"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

As we create more functions it starts to get a bit complicated to remember which
variables need to be passed into and out of each function. We are now going to do
something called refactoring. This means making significant design changes to our
code to make it easier to maintain in the future.

We are going to create a game state dictionary that includes all of the
information about the 'state' of the game and just pass this into and out of the
function.


Tasks:

1) Look at how the game state dictionary is created and how it has been passed
   into and out of the functions.
2) Modify all your functions to use the game state dicionary. You might find it
   useful to have this code and your code side by side in diffeent windows.
3) If you have written any extra functions yourself, try to modify them to use
   the game state dictionary.
4) Test it to make sure it works
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

def showStatus(game_state):
  """print out information about:
  where the player is,
  what the player has in their inventory,
  what items are available in the room.
  """
  currentRoom = game_state['currentRoom']
  inventory = game_state['inventory']
  rooms = game_state['rooms']

  print('---------------------------')
  print('You are in the ' + currentRoom)
  print('Inventory : ' + str(inventory))

  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])

  print("---------------------------")

def go(game_state):
    rooms = game_state['rooms']
    currentRoom = game_state['currentRoom']

    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      game_state['currentRoom'] = rooms[currentRoom][move[1]]

    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

    return game_state

def get(game_state):
    rooms = game_state['rooms']
    currentRoom = game_state['currentRoom']
    move = game_state['move']
    inventory = game_state['inventory']

    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to their inventory
        inventory.append(move[1])
        #display a helpful message
        print(move[1] + ' got!')
        #delete the item from the room
        del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
    else:
        #tell them they can't get it
        print('Can\'t get ' + move[1] + '!')

    return game_state

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'item': 'chair',
                },

            'Kitchen' : {
                  'north' : 'Hall'
                }

         }


game_state = {'rooms' : rooms, 'inventory': [], 'currentRoom': 'Hall'}

showInstructions()

while True:

  showStatus(game_state)

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  move = move.lower().split()
  game_state['move'] = move

  #if they type 'go' first
  if move[0] == 'go':
    game_state = go(game_state)

  #if they type 'get' first
  if move[0] == 'get' :
    game_state = get(game_state)
