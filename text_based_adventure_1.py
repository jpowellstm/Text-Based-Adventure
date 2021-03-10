"""
This is part of a series of files that builds up a text based adventure
programme based on https://projects.raspberrypi.org/en/projects/rpg. The rest of
the files can be found at https://github.com/jpowellstm/Text-Based-Adventure

This file will:

1) Define a function to print the commands that you can execute in the game.
2) Call the function to test it.

Tasks:

1) Think about what other commands might be necessary and add them. We can implement these later.
2) Think about a theme for your own text based adventure.
3) Modify the function to print out something for your theme.
4) Test it to make sure it works.
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


showInstructions()
