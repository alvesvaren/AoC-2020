import aoc
from collections import deque
from itertools import chain, islice
import inspect

p1, p2 = aoc.get_input(22).split("\n\n")

def parse_deck(data: str) -> deque:
    new_data = data.split("\n")[1:]
    return deque(map(int, new_data[::-1]))


deck1 = parse_deck(p1)
deck2 = parse_deck(p2)

orig_deck1, orig_deck2 = deck1.copy(), deck2.copy()

def play_game_recursive(deck1: deque, deck2: deque, mem: set=set()) -> tuple[int, deque, deque]:

    while len(deck1) != 0 and len(deck2) != 0:
        decks_as_tuples = tuple(deck1), tuple(deck2)
        if decks_as_tuples in mem:
            return (1, deck1, deck2)
        mem.add(decks_as_tuples)
        # print(len(inspect.stack()), deck1, deck2)
        card1 = deck1.pop()
        card2 = deck2.pop()
        # print(card1, card2)
        if len(deck1) >= card1 and len(deck2) >= card2:
            winner = play_game_recursive(
                deque(list(islice(deck1, card1 + 1))[:1]), 
                deque(islice(deck2, card2)), mem)
        
            if winner[0] == 1:
                deck1.appendleft(card1)
                deck1.appendleft(card2)
            elif winner[0] == 2:
                deck2.appendleft(card2)
                deck2.appendleft(card1)
            continue

        if card1 > card2:
            deck1.appendleft(card1)
            deck1.appendleft(card2)
        else:
            deck2.appendleft(card2)
            deck2.appendleft(card1)

        if len(deck2) == 0:
            return (1, deck1, deck2)
        if len(deck1) == 0:
            return (2, deck1, deck2)
    raise ValueError("Invalid input")

result, deck1, deck2 = play_game_recursive(deck1, deck2)
print(deck1, deck2)
sum1 = 0
for i,thing in enumerate(chain(deck1, deck2)):
    sum1 += thing*(i+1)
print(sum1)
