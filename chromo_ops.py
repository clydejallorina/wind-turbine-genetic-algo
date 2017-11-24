import random

class Chromosome:
    fitness = 0.0
    genes = [[0,0] , [0,0]]

    def __init__(self, genes):
        '''
        :type genes: List
        :param genes: A list of (x,y) floating point numbers. Required.
        '''
        self.genes = genes

    def set_fitness(self, new_fit):
        self.fitness = new_fit
        pass

    def get_fitness(self):
        return self.fitness

    def set_genes(self, list_of_genes=[[],[]]):
        self.genes = list_of_genes
        pass

    def get_genes(self):
        return self.genes

    def set_spec_gene(self, target, value):
        '''
        :param target: Gene X coordinate
        :param value: Value to set at coordinates
        '''
        self.genes[target] = value
        pass

    def get_spec_gene(self, target):
        return self.genes[target]

    def get_gene_length(self):
        return len(self.genes)

def crossover(chromo1, chromo2):
    #do stuff lol
    chromo1_length = chromo1.get_gene_length()
    chromo2_length = chromo2.get_gene_length()

    if chromo1_length > chromo2_length:
        target = random.randint(0,chromo2_length)
    else:
        target = random.randint(0,chromo1_length)
    gene1 = chromo1.get_spec_gene(target)
    gene2 = chromo2.get_spec_gene(target)
    chromo1.set_spec_gene(target, gene2)
    chromo2.set_spec_gene(target, gene1)
    pass

def mutate(chromo, num_of_mutations):
    #randomize and output

    #Choose a random X and Y to change
    target = random.randint(0,chromo.get_gene_length() - 1)
    value = [random.uniform(0,1), random.uniform(0,1)] #choose 2 values from 0 and 1
    print("Changing gene {} to {},{}", format(target, value[0], value[1]))
    chromo.set_spec_gene(target, value)
    pass

