from random import randint

from data.moves import Moves
from data.pokedex import Pokedex
from data.types import Types

blacklist = {'focuspunch','fakeout','snore','dreameater','lastresort','explosion','selfdestruct','synchronoise','belch','trumphcard','wringout'}
chargemoves = {'hyperbeam','gigaimpact','frenzyplant','blastburn','hydrocannon','rockwrecker','roaroftime','bounce','dig','dive','fly','freezeshock','geomancy','iceburn','phantomforce','razorwind','shadowforce','skullbash','skyattack','skydrop','solarbeam'}
def getMove(moves, pokemon, opponent):
    # Moves is a list of 4 moves, possibly good or bad moves...
    options = []
    for m in moves:
        if 'hiddenpower' in m:
            m = m[:-2]
        if m in blacklist or m in chargemoves:
            continue
        # Anything under 40 base power is probably useless (priority is 40)
        if (Moves[m]['basePower'] > 40 or m in ['grass knot', 'low kick']):
            options.append(m)
        if Moves[m]['type'] in Pokedex[pokemon.species]['types'] and Moves[m]['basePower'] > 0:
            options.append(m)
        if m not in options:
            continue
        # Resisted moves get 0 or 1 entry (1 only if STAB and over 40 base power)
        if len(Pokedex[opponent.species]['types']) > 1:
            types = Pokedex[opponent.species]['types']
            eff = Types[types[0]][Moves[m]['type']] * Types[types[1]][Moves[m]['type']]
            if eff < 1:
                options.remove(m)
        else:
            eff = Types[ Pokedex[opponent.species]['types'][0] ][Moves[m]['type']]
            if eff > 1:
                options.remove(m)
    if len(options) == 0:
        return moves[randint(0, len(moves)-1)]
    return options[randint(0, len(options)-1)]
        
def getLead(team, opposing):
    pass