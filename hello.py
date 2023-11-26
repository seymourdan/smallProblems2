import random

suits = ['S', 'C', 'D', 'H']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append([rank, suit])

    def shuffle(self):
        # shuffles deck of cards
        return random.sample(self.cards, 52)

# number of decks where the first ace is on the 14th draw
num_valid_decks = 0
num_15th_is8h = 0

# create 10,000,000 shuffled decks
# see how many of the decks, where the first ace is on the 14th draw, have 8h as the next card
for i in range(10_000_000):
    deck = Deck().shuffle()

    # excluding all decks with an ace not being on the 14th draw
    if deck[13][0] != 'A':
        continue

    # exlcuding all decks with an ace in the first 13 draws
    for j in range(13):
        if deck[j][0] == 'A':
            break
    else:
        num_valid_decks += 1
        #checking if 15th card is 8 of hearts
        if deck[14]== ['8', 'H']:
            num_15th_is8h += 1

# should be expecting 37/1824 = around 0.0191886
print(num_15th_is8h / num_valid_decks)