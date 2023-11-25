origin_deck = input().split()
step = int(input())
for suffle in range(step):
    middle_of_deck = len(origin_deck) // 2
    left_part = origin_deck [0:middle_of_deck]
    right_part = origin_deck [middle_of_deck:]
    shuffle_deck = []
    for card_index in range(len(left_part)):
        shuffle_deck.append(left_part[card_index])
        shuffle_deck.append(right_part[card_index])
        origin_deck = shuffle_deck
print(shuffle_deck)