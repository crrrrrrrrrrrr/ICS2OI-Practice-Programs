#12. dice game

# make it so that whenever you press x you exit no matter where in the code? (without copy paste code)

roll = 0
count = 0
again = "a"
import random
from getkey import getkey, keys

# intro to dice game
print ("""welcome to the dice game!
/press x at any time to exit the game/""")

# loop for playing again
while "x" not in again:
  # reset everything
  roll = 0
  count = 0
# get goal number
  print("""
____________________________
hit enter to roll for your goal # """)
  # if you press x you exit
  again = getkey()
  if again == "x":
    break
  
# roll for goal number
  goal = random.randrange(1, 7)
  print("your goal # is: " + str(goal) + """
""")

# instructions on how to play
  print("now try to roll a " + str(goal) + """ again in the least number of rolls
""")

  # loop for rolling for goal number
  while roll != goal:
    print("press enter to roll ")
    # if you press x you exit
    again = getkey()
    if again == "x":
      break
    # roll for number
    roll = random.randrange(1, 7)
    print("- you rolled a " + str(roll))
    # add up points
    count += 1
  # if pressed x, exit the play again loop
  if again == "x":
    break
  # if you rolled the goal number, congrats
  print("""
* congrats you rolled another """ + str(goal))
  print ("you rolled " + str(count) + " times!")
  
  # ask if they want to play again
  print ("""________________________________
if you want to exit press x""")
  # if you press x you exit
  again = getkey()
  if again == "x":
    break
# exited the game, thank you message
print ("thanks for playing!")
