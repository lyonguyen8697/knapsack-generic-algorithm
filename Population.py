from threading import Timer
from Chromosome import Chromosome
from ultis import pickRandom


class Population:
    chromosomes = []

    def __init__(self, size=20, elitism=0.2, maxWeight=1000, mutationRate=0.7):
        self.size = size
        self.elitism = elitism
        self.maxWeight = maxWeight
        self.mutationRate = mutationRate
        self.fill()

    def run(self, threshold = 1000, noImprovement=0, index=0, displayInterval=10):
        if noImprovement < threshold:
            lastScore = self.chromosomes[0].score
            self.generation()
            if lastScore >= self.chromosomes[0].score:
                noImprovement += 1
            else:
                noImprovement = 0
            if index % displayInterval == 0:
                self.display(index, noImprovement)
            index += 1
            Timer(0.001, self.run, (threshold, noImprovement, index)).start()
        else:
            self.display(index, noImprovement)

    def display(self, index, noImprovement):
        fitness = self.chromosomes[0]
        print "score: %d value: %d weight: %d generation: %d no change in: %d" % (fitness.score, fitness.value, fitness.weight, index, noImprovement)

    def generation(self):
        self.sort()
        self.kill()
        self.mate()
        self.fill()
        self.sort()

    def fill(self):
        length = len(self.chromosomes)
        while length < self.size:
            if length < self.size / 3:
                self.chromosomes.append(Chromosome(maxWeight=self.maxWeight, mutationRate=self.mutationRate))
            else:
                self.mate()
            length = len(self.chromosomes)

    def mate(self):
        parent1 = pickRandom(self.chromosomes)
        parent2 = pickRandom(self.chromosomes)
        while parent1 == parent2:
            parent2 = pickRandom(self.chromosomes)
        children = parent1.mate(parent2)
        self.chromosomes.append(children[0])
        self.chromosomes.append(children[1])

    def sort(self):
        self.chromosomes.sort(key=lambda e: e.score, reverse=True)

    def kill(self):
        target = int(self.elitism * len(self.chromosomes))
        while len(self.chromosomes) > target:
            self.chromosomes.pop()
