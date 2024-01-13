name1 = input("type first name: ").lower()
name2 = input("type second name: ").lower()

true_list = [letter for letter in "true"]
love_list = [letter for letter in "love"]


def compare(name):
    true_sum = 0
    love_sum = 0
    for letter in name:
        if letter in true_list:
            true_sum += 1
    for letter in name:
        if letter in love_list:
            love_sum += 1
    return true_sum, love_sum


final_outcome = compare(name1 + name2)
print(f"love score is: {final_outcome[0]}{final_outcome[1]}")
