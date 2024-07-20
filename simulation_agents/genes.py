import random


class Gene:
    def __init__(self, value, mutationForceChanges):
        self.value = value
        self.mutationForceChanges = mutationForceChanges

    def geneMutation(self):
        self.value *= random.randint(1 - self.mutationForceChanges, 1 + self.mutationForceChanges)


class GeneCluster:
    def __init__(self, genes):
        self.genes = genes

    def clasterMutation(self):
        geneIndex = random.randint(0, len(self.genes) - 1)
        self.genes[geneIndex].geneMutation()

    def addGenes(self, genes):
        self.genes.extend(genes)
