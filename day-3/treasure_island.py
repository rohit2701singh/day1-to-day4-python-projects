print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")
print("you are on the crossroad.")

crossroad = input("choose the direction where you want to go? right or left? \n").lower()
if crossroad == "right":
    print("\nsorry! you choose the wrong direction. you fell into hole.\n GAME OVER.")
elif crossroad == "left":
    print("\nyou have arrived at the river bank.")

    river_bank = input("\nyou want to wait or swim? ").lower()
    if river_bank == "swim":
        print("\nsorry! swimming was a dangerous choice.\n GAME OVER.")
    elif river_bank == "wait":
        print("\nA boat came and now you have arrived at the Island.\nThere are three doors in front of you. only one "
              "door can lead you towards treasure.")

        door = input("\nwhich door do you want to open? blue, red or yellow? ").lower()
        if door == "red" or door == "blue":
            print("\nsorry! you opened the wrong door. you are killed by monsters.\n GAME OVER")
        elif door == "yellow":
            print("\nCONGRATS ! you have cleared all the hurdles and reached your destination.\nYOU FOUND THE "
                  "TREASURE.\n💵🏆==$$++$$==💵🏆")
        else:
            print("\nchoosing choice other than provided lead you in maze.\n GAME OVER")

    else:
        print("\neither 'wait' or 'swim'. you have no other choice.\n GAME OVER")
else:
    print("you have chosen direction other than the provided one.\n GAME OVER")
