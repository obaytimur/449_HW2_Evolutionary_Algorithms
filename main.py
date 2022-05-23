# imported libraries
import cv2
from matplotlib import pyplot as plt
from copy import deepcopy as kopya
import functions
import os

# Constants, global variables, and changing parameters

num_inds_list = [5, 10, 20, 50, 75]
num_genes_list = [10, 25, 50, 100, 150]
tm_size_list = [2, 5, 10, 20]
frac_elites_list = [0.05, 0.2, 0.4]
frac_parents_list = [0.2, 0.4, 0.6, 0.8]
mutation_prob_list = [0.1, 0.2, 0.5, 0.8]
mutation_type_list = ["guided", "unguided"]
parameter_list_list = [num_inds_list, num_genes_list, tm_size_list, frac_elites_list, frac_parents_list,
                       mutation_prob_list, mutation_type_list]
parameter_name_list = ["default", "num_inds", "num_genes", "tm_size", "frac_elites", "frac_parents", "mutation_prob",
                       "mutation_type"]
parameter_change_name_list = [["5", "10", "20", "50", "75"],
                              ["10", "25", "50", "100", "150"],
                              ["2", "5", "10", "20"],
                              ["0.05", "0.2", "0.4"],
                              ["0.2", "0.4", "0.6", "0.8"],
                              ["0.1", "0.2", "0.5", "0.8"],
                              ["guided", "unguided"],
                              [""]]


def evolution(num_inds, num_genes, tm_size, frac_elites, frac_parents, mutation_prob, mutation_type, parameter_name,
              parameter_change_name):
    img_source = cv2.imread("painting.png")
    fitness_plot = []
    plot_mode = 100
    num_generations = 10000
    save_path = "img_results/" + parameter_name
    # Start of Evolution

    # Population creation
    population = functions.create_pop(num_inds, num_genes)

    # loop for improving generation
    for generation in range(num_generations + 1):
        population = functions.evaluate_pop_fitness(population)
        size_population = len(population)

        elite_list, remain_list = functions.elite_select(population, frac_elites)

        size_elite = len(elite_list)
        size_remain = len(remain_list)
        size_parents = int(size_population * frac_parents)
        size_mutation = size_remain - size_parents

        tournament_result = functions.remain_select(remain_list, tm_size, size_remain)
        parents_list, non_parents_list = tournament_result[0:size_parents], tournament_result[size_parents:]
        children_list = functions.crossover_pop(parents_list)

        mutated_children = functions.mutation_pop(mutation_type, mutation_prob, children_list, num_genes)
        mutated_non_parent = functions.mutation_pop(mutation_type, mutation_prob, non_parents_list, num_genes)

        next_population = kopya(functions.evaluate_pop_fitness(elite_list + mutated_children + mutated_non_parent))
        next_population = sorted(next_population, key=lambda item: item.fitness, reverse=True)

        if generation % 1000 == 0:
            print(parameter_name + " " + parameter_change_name + "Generation %4d is done" % generation)
            cv2.imwrite(os.path.join(save_path, parameter_name + "_" + parameter_change_name + '_Generation_' + str(
                generation) + '.png')
                        , next_population[0].evaluate_ind())

        if generation % plot_mode == 0:
            fitness_plot.append(next_population[0].fitness)

        population = kopya(next_population)

    plt.figure(1)
    plt.ylabel("Fitness Values")
    plt.xlabel("Generation from 1 to 1k")
    plt.plot(fitness_plot[0:10])
    plt.savefig(os.path.join(save_path, parameter_name + "_" + parameter_change_name + '_Fitness_1_to_1k' + '.png'))
    plt.close(1)

    plt.figure(2)
    plt.ylabel("Fitness Values")
    plt.xlabel("Generation from 1k to 10k")
    plt.plot(fitness_plot[10:100])
    plt.savefig(os.path.join(save_path, parameter_name + "_" + parameter_change_name + '_Fitness_1k_to_10k' + '.png'))
    plt.close(2)

    return None


# Default evolution
evolution(num_inds_list[2], num_genes_list[2], tm_size_list[1], frac_elites_list[1], frac_parents_list[2],
          mutation_prob_list[1], mutation_type_list[0], parameter_name_list[0], parameter_change_name_list[7][0])

# num_inds evolutions
for index in range(5):
    if index != 2:
        evolution(num_inds_list[index], num_genes_list[2], tm_size_list[1], frac_elites_list[1], frac_parents_list[2],
                  mutation_prob_list[1], mutation_type_list[0], parameter_name_list[1],
                  parameter_change_name_list[0][index])

for index in range(5):
    if index != 2:
        evolution(num_inds_list[2], num_genes_list[index], tm_size_list[1], frac_elites_list[1], frac_parents_list[2],
                  mutation_prob_list[1], mutation_type_list[0], parameter_name_list[2],
                  parameter_change_name_list[1][index])

for index in range(4):
    if index != 1:
        evolution(num_inds_list[2], num_genes_list[2], tm_size_list[index], frac_elites_list[1], frac_parents_list[2],
                  mutation_prob_list[1], mutation_type_list[0], parameter_name_list[3],
                  parameter_change_name_list[2][index])

for index in range(3):
    if index != 1:
        evolution(num_inds_list[2], num_genes_list[2], tm_size_list[1], frac_elites_list[index], frac_parents_list[2],
                  mutation_prob_list[1], mutation_type_list[0], parameter_name_list[4],
                  parameter_change_name_list[3][index])

for index in range(4):
    if index != 2:
        evolution(num_inds_list[2], num_genes_list[2], tm_size_list[1], frac_elites_list[1], frac_parents_list[index],
                  mutation_prob_list[1], mutation_type_list[0], parameter_name_list[5],
                  parameter_change_name_list[4][index])

for index in range(4):
    if index != 1:
        evolution(num_inds_list[2], num_genes_list[2], tm_size_list[1], frac_elites_list[1], frac_parents_list[2],
                  mutation_prob_list[index], mutation_type_list[0], parameter_name_list[6],
                  parameter_change_name_list[5][index])

for index in range(2):
    if index != 0:
        evolution(num_inds_list[2], num_genes_list[2], tm_size_list[1], frac_elites_list[1], frac_parents_list[2],
                  mutation_prob_list[1], mutation_type_list[index], parameter_name_list[7],
                  parameter_change_name_list[6][index])

print("Evolutions are finished.")
