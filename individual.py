from gene import gene
import numpy as np
# individual class declaration
# there are multiple functions to control individuals


class individual:
    def __init__(self, num_genes, fitness = 0):
        chromosome = []
        for index in num_genes:
            gene_var = gene
            gene_var.rand_value()
            while not gene_var.is_in_image():
                gene_var.rand_value()
            chromosome.append(gene_var)
        self.evaluate_fitness()

    def evaluate_ind(self):

    def evaluate_fitness(self, source_image, image):

        fitness = -1 * np.sum(np.square(source_image - image))











