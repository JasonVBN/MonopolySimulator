import random
from info import NAMES

def comchest():
    return random.randint(0,39)
def chance():
    return random.randint(0,39)
def jail():
    return 10
JUMPS = {
    2: comchest,
    7: chance,
    17: comchest,
    22: chance,
    30: jail,
    33: comchest,
    36: chance
}


## simulation parameters ##
PLAYERS = 4
TURNS = 1000

def diceRoll(numDice=2):
    return sum(random.randint(1,6) for i in range(numDice))

pos = [0 for p in range(PLAYERS)]
timesVisited = [0 for i in range(40)]
# ex. 0 = start square (GO), 5 = Reading Railroad, etc.

for turn in range(TURNS):
    for player in range(PLAYERS):
        rolled = diceRoll()
        newpos = (pos[player]+rolled) % 40
        timesVisited[newpos] += 1
        if newpos in JUMPS:
            # print(f"hit special square at {newpos}")
            newpos = JUMPS[newpos]()
            timesVisited[newpos] += 1
        pos[player] = newpos

ordered = []
for i,n in enumerate(timesVisited):
    print(f"{i}: {n}")
    ordered.append((i,n))
ordered.sort(key=lambda tup: tup[1], reverse=True)
print("\nORDERED BY NUM VISITS:")
for i,freq in ordered:
    print(f"{i} ({NAMES[i]}): {freq}")
