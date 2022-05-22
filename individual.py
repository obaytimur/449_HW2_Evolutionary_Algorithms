# Imports for the individual class
import cv2
from gene import gene
import numpy as np
from copy import deepcopy as kopya


# function to create a white image with the same size of original one
def white_img():
    global height, width
    img_white = np.ones((height, width,3), np.uint8)
    img_white[:] = 255
    return kopya(img_white)


# individual class declaration
class individual:

    def __init__(self, num_genes, fitness=None, chromosome=None):
        self.fitness = fitness
        if chromosome is None:
            chromosome = []
            for index in num_genes:
                gene_var = gene
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
            drawing_img = img_init
            cv2.circle(drawing_img, center=(index().x, index().y), radius=index().radius,
                       color=( index().blue, index().green,index().red), thickness=-1)
            img_init = cv2.addWeighted(drawing_img, index().alpha, img_init, 1-index().alpha, 0)
        return img_init

    def evaluate_fitness(self):
        global img_source
        fitness = -1 * np.sum(np.square(img_source - self.evaluate_ind()))
        self.fitness = fitness














