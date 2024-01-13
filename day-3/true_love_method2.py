name1 = input("your name: ").lower()
name2 = input("their name: ").lower()

joined_list = ["true", "love"]

true_love = []
total_sum = 0

for i in range(len(joined_list)):
    for letter in joined_list[i]:
        letter_count = (name1 + name2).count(letter)
        total_sum += letter_count
    true_love.append(total_sum)

    print(f"{joined_list[i]}_sum: {total_sum}")
    total_sum = 0

print(f"your love score is: {true_love[0]}{true_love[1]}.")
