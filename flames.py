def relation(names):
    acronym = ['F', 'L', 'A', 'M', 'E', 'S']
    meanings = {
        'F': "Friend", 'L': "Lover", 'A': "Attraction", 'M': "Marriage", 'E': "Enemy", 'S': "Sibling"
    }

    names = names.lower().replace(" ", "")
    while len(acronym) > 1:
        index = len(names) % len(acronym) - 1
        if index == -1:
            acronym.pop(index)
        else:
            acronym.pop(index)
            acronym = acronym[index:]+acronym[:index]

    relationship = acronym[0]
    return meanings[relationship]


def same_letters(name1, name2):
    new_name1 = list(name1)
    new_name2 = list(name2)

    for letter in name1:
        if letter in new_name2:
            new_name1.remove(letter)
            new_name2.remove(letter)

    return "".join(new_name1), "".join(new_name2)


print("Game of Flame!")
print("Know Your Relationship..")
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

relationship = relation(name1 + name2)

print("Relationship between " + name1 + " & " + name2 + " is: " + relationship)