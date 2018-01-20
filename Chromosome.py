import json
from copy import deepcopy
from random import random, randint
from ultis import pickRandom

elements = {}
with open("elements.json") as f:
    elements = json.load(f)


class Chromosome:
    weight = 0
    value = 0
    score = 0

    def __init__(self, members=None, maxWeight=1000, mutationRate=0.7):
        if not members:
            self.random()
        else:
            self.members = members
        self.maxWeight = maxWeight
        self.mutationRate = mutationRate
        self.mutate()
        self.calcScore()

    def random(self):
        self.members = deepcopy(elements)
        for member in self.members.itervalues():
            member["active"] = random() < 0.5

    def mutate(self):
        if random() > self.mutationRate:
            return
        member = pickRandom(self.members)
        member["active"] = not member["active"]

    def calcScore(self):
        self.weight = 0
        self.value = 0
        self.score = 0
        for member in self.members.itervalues():
            if member["active"]:
                self.value += member["value"]
                self.weight += member["weight"]
        self.score = self.value
        if self.weight > self.maxWeight:
            self.score -= (self.weight - self.maxWeight) * 50
        return self.score

    def mate(self, other):
        child1 = {}
        child2 = {}
        pivot = randint(0, len(self.members) - 1)
        index = 0
        for key in elements.keys():
            if index < pivot:
                child1[key] = self.members[key].copy()
                child2[key] = other.members[key].copy()
            else:
                child2[key] = self.members[key].copy()
                child1[key] = other.members[key].copy()
            index += 1
        child1 = Chromosome(child1, self.maxWeight, self.mutationRate)
        child2 = Chromosome(child2, self.maxWeight, self.mutationRate)
        return [child1, child2]
