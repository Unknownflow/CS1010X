cards = ('QS', 'AC', 'TD', 'JC', 'KH')

def card_magician(output, cards, trick):
    for card in cards:
        output = trick(output, card)
    return output

def compare_cards(card1, card2):
    c1 = 'Z' if card1[0] == 'A' else card1[0]
    c1 = 'Y' if card1[0] == 'K' else c1
    c1 = 'B' if card1[0] == 'T' else c1
    c2 = 'Z' if card2[0] == 'A' else card2[0]
    c2 = 'Y' if card2[0] == 'K' else c2
    c2 = 'B' if card2[0] == 'T' else c2
    return card1[1] > card2[1] if c1 == c2 else c1 > c2

def sort_deck(deck):
    a = (deck[0], ) 
    b = deck[1:]
    c = lambda x, y: (x, y if compare_cards(x,y) else y, x)
    return card_magician(a, b, c)

# Uncomment the following line.
sorted_deck = sort_deck(cards)
print(sorted_deck)

print(sort_deck((('AS', '5S', 'TS', '7S'))))