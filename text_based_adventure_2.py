"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

This file will:

1) Add in data structures for:
- the inventory of items that the player carries,
- the available rooms and how they link together,
- the current room that the player is in.


Tasks

1) Modify the rooms fit the theme you cam up with previously.
2) Write down what data structures are being used for inventory, rooms, and
currentRoom.
3) Draw a map of your world on paper to help you code it.
4) Add some extra rooms and the links between them.
5) Add an item field to the dictionary and give your rooms some items.
6) Test it to make sure it works. You need to make sure that you can navigate
to the extra rooms.
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
