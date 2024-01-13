print("welcome to the tip calculator.")

bill = float(input("what was the total bill? ₹ "))
tip = float(input("what percentage tip would you like to give? 10, 12 or 15 ? "))

total_tip = bill * tip / 100
total_pay = total_tip + bill
print(f"tip you want to give is= ₹{total_tip}")
print(f"your total bill is= ₹{total_pay}")

people = int(input("how many people to split the bill= "))
each_pay = round(total_pay / people, 2)

print(f"each person should pay= ₹{each_pay}")
