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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to treasure island")
print('you\'ve arrived at a crossroad, you can only choose one direction to move forward to choose your direction "Left" or "Right"')
path = input("Choose your direction: ").lower()
if path == 'left':
    print("You have survived and have arrived near the river, you can waith for the boat or can swim. choose thoughtfully")
    river = input('Do you want to "wait" or "swim"?\n').lower()
    if river == 'wait':
        print("You are just one step away from finding the treasure choose the correct door to open and be a treasure hunter")
        choice3 = input('choose which door to open "Yellow", "Blue" or "Green": ').lower()
        if choice3 == 'blue':
            print("Congratulations you have found the treasure!, You Win!")
        elif choice3 =='yellow':
            print("You have opend the gate of Hell for yourself")
        elif choice3 =="green":
            print("You have been eaten alive by a hungry Lion")
        else:
            print("You choose a door that dosen't exist, Game Over")
    else:
        print("You have drowned")
else:
    print("An Hungry Bear has killed you")