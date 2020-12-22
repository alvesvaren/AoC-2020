import aoc
from collections import deque

p1, p2 = aoc.get_input(22).split("\n\n")

def parse_deck(data: str) -> deque:
    new_data = data.split("\n")[1:]
    return deque(map(int, new_data[::-1]))


deck1 = parse_deck(p1)
deck2 = parse_deck(p2)

while len(deck1) != 0 and len(deck2) != 0:
    card1 = deck1.pop()
    card2 = deck2.pop()

    if card1 > card2:
        winning_deck = deck1
    else:
        winning_deck = deck2

    winning_deck.appendleft(max(card1, card2))
    winning_deck.appendleft(min(card1, card2))

sum1 = 0
for i,thing in enumerate(max(deck1, deck2, key=len)):
    sum1 += thing*(i+1)
print(sum1)
