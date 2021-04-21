"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

We are going to add a drop function to allow the player to drop an item they have
in thier inventory in the room they are in.


Tasks:

1) Update the show instructions function so it prints the drop function details
2) Add the drop function
3) Test it to make sure it works
4) Can you find any bugs or limitations with the game at the moment?
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
  drop [item]

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

def drop(game_state):
    currentRoom = game_state['currentRoom']
    move = game_state['move']
    inventory = game_state['inventory']

    if move[1] in inventory:
        inventory.remove(move[1])
        game_state['rooms'][currentRoom]['item'] = move[1]

    return game_state

#a dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'item': 'chair',
                },

            'Kitchen' : {
                  'north' : 'Hall',

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

  if move[0] == 'drop' :
    game_state = drop(game_state)
