print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
******************************************************************************* ''')
print(" Welcome to the treasure island")
print("Your challange is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".  ')

if choice1 == "left":
    # Continue in the game
   choice2 = input('You\'ve come to a lake There is an island in thr middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
if choice2 == "wait":
    # Game will Continue
     choice3 = input("You arrive at the island unharmed. There is a House with 3 Doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
     if choice3 == "red":
         print("It's a room full of fire. Game Over.")
     elif choice3 == "yellow":
           print("You found the Treasure!. You win!")
     elif choice3 == "blue":
           print("You enter in a room full of Beats. Game over.")
     else:
         print("You got attacked by an Angry trout. Game Over ")
else:
    print("you fell into a hole. Game Over.")

