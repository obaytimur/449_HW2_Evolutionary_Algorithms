# Imports for the individual class
import cv2
from gene import gene
import numpy as np
from copy import deepcopy as kopya


# function to create a white image with the same size of original one
def white_img():
    img_white = np.ones((180, 180, 3), np.uint8)
    img_white[:] = 255
    return kopya(img_white)


# individual class declaration
class individual:

    def __init__(self, num_genes=None, fitness=0, chromosome=None):
        self.fitness = fitness
        if chromosome is None:
            chromosome = []
            for index in range(num_genes):
                gene_var = gene()
                gene_var.rand_value()
                while not gene_var.is_in_image():
                    gene_var.rand_value()
                chromosome.append(gene_var)
        self.chromosome = chromosome
        self.evaluate_fitness()

    def evaluate_ind(self):
        gene_sorted = sorted(self.chromosome, key=lambda item: item.radius, reverse=True)
        img_init = white_img()
        for index in gene_sorted:
            drawing_img = kopya(img_init)
            drawing_img = cv2.circle(drawing_img, (index.x, index.y), index.radius, (index.blue, index.green, index.red),-1)
            img_init = cv2.addWeighted(drawing_img, index.alpha, img_init, 1-index.alpha, 0)
        return img_init

    def evaluate_fitness(self):
        img_source = cv2.imread("painting.png")
        fitness = -1 * np.sum(np.square(img_source - self.evaluate_ind()))
        self.fitness = fitness
