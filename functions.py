import random

from individual import individual
from copy import deepcopy as kopya


def create_pop(num_inds, num_genes):
    pop_list = []
    for index in range(len(num_inds)):
        ind_var = individual(num_genes)
        pop_list.append(kopya(ind_var))
    return pop_list


def evaluate_pop_fitness(pop_list):
    for index in pop_list:
        index().evaluate_fitness()
    return pop_list


def evaluate_pop(pop_list):
    chromosome_list = []
    for index in pop_list:
        chromosome_list = chromosome_list + index.chromosome
    pop_individual = individual(num_genes=len(chromosome_list), chromosome=chromosome_list)
    image = pop_individual.evaluate_ind()
    return image


def elite_select(pop_list, frac_elites):
    elite_size = int(len(pop_list)*frac_elites)
    pop_sorted = sorted(kopya(pop_list), key=lambda item: item.fitness, reverse=True)
    return pop_sorted[0:elite_size], pop_sorted[elite_size:]


def remain_select(pop_list, tm_size, selection_size):
    selected_list = []
    for index in range(selection_size):
        random.shuffle(pop_list)
        pop_list = pop_list[0:tm_size]
        sorted_pop_list = sorted(pop_list, key=lambda item: item.fitness, reverse=True)
        selected_list.append(kopya(sorted_pop_list[0]))
    return selected_list


def crossover_two_parent(parent1, parent2):
    parent1_gene = parent1.chromosome
    parent2_gene = parent2.chromosome
    child1_gene = individual(chromosome=parent1_gene, num_genes=len(parent1_gene))
    child2_gene = individual(chromosome=parent2_gene, num_genes=len(parent2_gene))

    for index in range(len(parent1_gene)):
        if random.random() > 0.5:
            temp = kopya(child1_gene.chromosome[index])
            child1_gene.chromosome[index] = kopya(child2_gene.chromosome[index])
            child2_gene.chromosome[index] = kopya(temp)

    return [child1_gene, child2_gene]


def crossover_pop(pop_list):
    child_list = []
    for index in range(len(pop_list)):
        child_list.append(crossover_two_parent(pop_list[index*2], pop_list[index*2 + 1]))
    return child_list


def mutation_gene(mutation_type, mutated_gene):
    if mutation_type == "unguided":
        mutated_gene.rand_value()
        return mutated_gene
    else:
        mutated_gene.x += random.randint(int(-0.25*mutated_gene.x), int(0.25*mutated_gene.x))
        mutated_gene.y += random.randint(int(-0.25*mutated_gene.y), int(0.25*mutated_gene.y))
        mutated_gene.radius = random.randint(max(0, mutated_gene.radius-10), max(0, mutated_gene.radius+10))
        mutated_gene.red = random.randint(max(0, mutated_gene.red-64), min(255, mutated_gene.red+64))
        mutated_gene.green = random.randint(max(0, mutated_gene.green-64), min(255, mutated_gene.green+64))
        mutated_gene.blue = random.randint(max(0, mutated_gene.blue-64), min(255, mutated_gene.blue+64))
        mutated_gene.alpha += random.uniform(max(0, mutated_gene.alpha-0.25), min(1, mutated_gene.alpha+0.25))
        return mutated_gene


def mutation_ind(mutation_type, mutation_prob, indiv: individual, num_genes):
    if random.random() < mutation_prob:
        mutation_index = random.randint(0, num_genes-1)
        indiv.chromosome[mutation_index] = mutation_gene(mutation_type, indiv.chromosome[mutation_index])
    return indiv


def mutation_pop(mutation_type, mutation_prob, pop_list: list, num_genes):
    for index in range(len(pop_list)):
        mutation_ind(mutation_type, mutation_prob, pop_list[index], num_genes)
    return None








