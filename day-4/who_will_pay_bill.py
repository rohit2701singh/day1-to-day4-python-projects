import random

name = input("enter all members names with comma b/w them?")
name_list = name.split(",")
print(f"member_list= {name_list}")

total_members = len(name_list)
print(f"total members= {total_members}")

selected_member = random.choice(name_list)
print(f"{selected_member} is going to pay the food bill.")
