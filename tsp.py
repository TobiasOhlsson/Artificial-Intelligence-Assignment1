import fileinput
import random

import numpy as np

is_euclidean = False
number_of_cities = 0
cities = []

for i, line in enumerate(fileinput.input()):
    line = line.rstrip()
    if i == 0:
        is_euclidean = (line == 'euclidean')
    elif i == 1:
        number_of_cities = int(line)
        distance_matrix = np.zeros((number_of_cities, number_of_cities))
    elif i < (number_of_cities + 2):
        c = line.split()
        cities.append((float(c[0]), float(c[1])))
    elif i < (2 * number_of_cities + 2):
        s = line.split()
        a = i - (number_of_cities + 2)
        for j, d in enumerate(s):
            distance_matrix[a][j] = d


def create_tsp(front_node, back_node, matrix):
    tour = str(front_node)
    total_distance = 0
    for k in range(number_of_cities):
        min_position_front = [0, 0]
        min_position_back = [0, 0]
        min_value_front = float("inf")
        min_value_back = float("inf")
        for i in range(number_of_cities):
            if (matrix[front_node][i] < min_value_front) & (matrix[front_node][i] != -1) & (front_node != i):
                min_value_front = matrix[front_node][i]
                min_position_front = i
            if (matrix[back_node][i] < min_value_back) & (matrix[back_node][i] != -1) & (back_node != i):
                min_value_back = matrix[back_node][i]
                min_position_back = i
        if min_value_front < min_value_back:
            matrix[:, front_node] = -1
            tour = tour + " " + str(min_position_front)
            front_node = min_position_front
            total_distance += min_value_front
        else:
            matrix[:, back_node] = -1
            tour = str(min_position_back) + " " + tour
            back_node = min_position_back
            total_distance += min_value_back
    return tour, total_distance


best_score = float("inf")
for time in range(number_of_cities):
    #front_node = random.randint(0, number_of_cities)
    front_node = time
    back_node = front_node
    matrix = np.copy(distance_matrix)
    t, score = create_tsp(front_node, back_node, matrix)
    if score < best_score:
        best_score = score
        print(t)
        #print(score)
