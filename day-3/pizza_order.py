print("welcome to python pizza delivers!")

sbill = 0
bill = 0
size = input("what size of pizza do you want? s(small), m(medium), l(large): ")

if size == "s" or size == "m" or size == "l":
    if size == "s":
        sbill = 15
    elif size == "m":
        bill = 20
    else:
        bill = 25

    pepperoni = input("do you want pepperoni? y or n: ")
    if pepperoni == "y" or pepperoni == "n":
        if pepperoni == "y":
            if size == "s":
                sbill += 2
            else:
                bill += 3
        cheese = input("do you want extra cheese? y or n = ")
        if cheese == "y" or cheese == "n":
            if cheese == "y":
                if size == "s":
                    sbill += 1
                else:
                    bill += 1

            if size == "s":
                print(f"your final bill is: ${sbill}")
            else:
                print(f"your final bill is: ${bill} ")

        else:
            print("please choose from given option.")
    else:
        print("please choose from given option.")
else:
    print("* Program is case sensitive. Please choose the correct letter.")
