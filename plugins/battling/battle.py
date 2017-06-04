class Pokemon:
    def __init__(self, ident, details, condition, active, stats, moves, baseAbility, item, canMegaEvo, slot, side):
        self.species = ident
        self.details = details
        self.condition = condition.split()[0]
        self.status = condition.split()[1] if ' ' in condition else ''
        self.active = active
        self.stats = stats
        self.moves = moves
        self.ability = baseAbility
        self.item = item
        self.canMega = canMegaEvo
        self.teamSlot = slot
        self.side = side
        self.boosts = {'atk':0, 'def':0, 'spa':0, 'spd':0, 'spe':0, 'evasion':0, 'accuracy':0}
    def clearBoosts(self):
        self.boosts = {'atk':0, 'def':0, 'spa':0, 'spd':0, 'spe':0, 'evasion':0, 'accuracy':0}
    def setCondition(self, cond, status):
        self.condition = cond
        self.status = status

class Player:
    def __init__(self):
        self.name = ''
        self.id = ''
        self.canZmove = True
        self.canMegaPokemon = True
        self.active = None
        self.team = {}
        self.side = {}
    def setActive(self, poke):
        self.active = poke
    def updateTeam(self, poke):
        if poke.species in self.team:
            poke.boosts = self.team[poke.species].boosts
        self.team[poke.species] = poke
    def changeTeamSlot(self, old, new):
        if not old:
            for m in self.team:
                if self.team[m]:
                    old = self.team[m]
        old.teamSlot, new.teamSlot = new.teamSlot, old.teamSlot
    def getPokemon(self, species):
        for poke in self.team:
            if self.team[poke].species == species:
                return self.team[poke]
        # Logically this shouldn't happen, but apparently it does sometimes?
        raise AttributeError('{mon} isn\'t in the team'.format(mon = species))
    def removeBaseForm(self, pokemon, mega):
        self.team[mega] = self.team.pop(pokemon, None)
        self.team[mega].species = mega
        self.canMegaPokemon = False

    def usedZmove(self):
        self.canZmove = False

class Battle:
    def __init__(self, name):
        self.rqid = 1
        self.myActiveData = {}
        self.me = Player()
        self.other = Player()
        self.field = {}
        self.spectating = False
        self.ladderGame = False

    def setMe(self, me, pId):
        self.me.name = me
        self.me.id = pId
    def setOther(self, other, pId):
        self.other.name = other
        self.other.id = pId
    def isLadderMatch(self):
        self.ladderGame = True
    def setFieldCond(self, cond):
        # TODO: do this
        pass

