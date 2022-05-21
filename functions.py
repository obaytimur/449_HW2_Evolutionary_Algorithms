from individual import individual
from copy import deepcopy as kopya


def create_pop(num_inds, num_genes):
    pop_list = []
    for index in range(len(num_inds)):
        ind_var = individual(num_genes)
        pop_list.append(kopya(ind_var))
    return pop_list


def evaluate_pop(pop_list):
    for index in range(len(pop_list)):
        index.cal