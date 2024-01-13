height = int(input("what is your height (in cm)? "))
age = int(input("what is your age? "))

bill = 0
if height > 120:
    print("your can ride the bike.")
    if age < 12:
        bill = 5
        print("\nfor child ticket pay 5$. ")
    elif age < 18:
        bill = 7
        print("\nfor youth ticket pay 7$.")
    elif age > 45 and age < 50:
        bill += 0
        print("you have nothing to pay for this ride.")
    else:
        print("for adult ticket pay 12$.")
        bill = 12

    photo = input("\ndo you want a photo? you'll have to pay extra 3$. y/n? ")
    if photo == "y":    # add 3$ to their bill.
        bill += 3
    print(f"your final bill is ${bill}")
else:
    print("\nyou are short.you can't ride.")
