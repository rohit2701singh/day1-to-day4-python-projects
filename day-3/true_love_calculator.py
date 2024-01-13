name1 = input("type first name: ").lower()
name2 = input("type second name: ").lower()


def calculate(comparing_word):
    sum = 0
    for letter in comparing_word:
        com_letter = (name1 + name2).count(letter)
        print(f"{letter}: {com_letter}")
        sum += com_letter
    print(f"{comparing_word}_sum: {sum}")
    return sum


true = calculate("true")
love = calculate("love")
print(f"your love score is: {true}{love}")

