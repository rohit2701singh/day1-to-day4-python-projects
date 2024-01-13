line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

treasure_map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot. ")
position = input("Where do you want to put the treasure (column,row) e.g. B3: ").upper()

abc_list = ["A", "B", "C"]

column = int(abc_list.index(position[0]))
row = int(position[1]) - 1

treasure_map[row][column] = "X"

print(f"{line1}\n{line2}\n{line3}")
