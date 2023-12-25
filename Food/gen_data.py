from random import choice
prefix1 = ['Beauty', 'Big', 'Brave', 'Bright', 'Charming', 'Cold', 'Cool', 'Exciting', 'Fresh', 'Gorgeous', 'Hot', 'Huge', 'Important', 'Kind', 'Leading', 'Light', 'Lucky', 'Marvel', 'Nice', 'Old', 'Perfect', 'Rare', 'Safe', 'Small', 'Steel', 'Stone', 'Strange', 'Sweet', 'Tiny', 'True', 'Warm', 'Wise', 'Wonderful']
prefix2 = ["Black", "White", "Red", "Green", "Yellow", "Blue", "Brown", "Orange", "Pink", "Purple", "Grey"]
root = ['Book', 'Car', 'Castle', 'City', 'Day', 'Door', 'Game', 'Hand', 'Head', 'Home', 'House', 'Level', 'Line', 'Mind', 'Moment', 'Morning', 'Name', 'Night', 'Number', 'Paper', 'Part', 'Point', 'Power', 'Process', 'Result', 'Sense', 'Side', 'Story', 'Table', 'Team', 'Water', 'Way', 'Week', 'Word', 'World', 'Year']
for i in range(10):
    print(choice(prefix1) + choice(prefix2) + choice(root))


vowel = ['a', 'e', 'i', 'o', 'u']
consonant = [chr(ord('a')+ i) for i in range(26) if chr(ord('a')+ i) not in vowel]
obr = "LIPTON"
for i in range(10):
    res = choice(consonant) + choice(vowel) + choice(consonant) + choice(consonant) + choice(vowel) + choice(consonant)
    print(''.join(res))