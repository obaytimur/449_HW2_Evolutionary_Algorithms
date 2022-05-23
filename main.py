# imported libraries
import cv2
from matplotlib import pyplot as plt
from copy import deepcopy as kopya
import functions

# Constants, global variables, and changing parameters
img_source = cv2.imread("painting.png")

num_inds = 20
num_genes = 50
tm_size = 5
frac_elites = 0.2
frac_parents = 0.6
mutation_prob = 0.2
mutation_type = "guided"
parameter_name = "default"

num_generations = 10000

save_path = "img_results/default"
plot_mode = 50

fitness_plot = []

# Start of Evolution

# Population creation
population = functions.create_pop(num_inds, num_genes)

# loop for improving generation
for generation in range(num_generations + 1):
    population = functions.evaluate_pop(population)
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

    next_population = kopya(functions.evaluate_pop(elite_list + mutated_children + mutated_non_parent))
    next_population = sorted(next_population, key=lambda item: item.fitness, reverse=True)

    if generation % 1000 == 0:
        drawn_img = next_population[0].evaluate_ind
        cv2.imwrite(save_path + parameter_name + "_generation" + str(generation) + ".png", drawn_img)

    if generation % plot_mode == 0:
        fitness_plot.append(next_population[0].fitness)

    population = kopya(next_population)

plt.figure(1)
plt.ylabel("Fitness Values")
plt.xlabel("Generation from 1 to 10k")
plt.plot(fitness_plot)
plt.savefig(save_path + parameter_name + "_Fitness_1_10k.png")
plt.close(1)

plt.figure(2)
plt.ylabel("Fitness Values")
plt.xlabel("Generation from 1k to 10k")
plt.plot(fitness_plot)
plt.savefig(save_path + parameter_name + "_Fitness_1k_10k.png")
plt.close(2)
