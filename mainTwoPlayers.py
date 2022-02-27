import os
import random
import time
from datetime import datetime
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

from environment.Graph2 import Graph2
from environment.Transition import Transition
from players.DQN.DQN import GRID_SIZE, WINDOW_SIZE, TEST_MODE
from players.DQN.DqnPlayer import DqnPlayer, convert_data_to_state, NOT_LEGAL_STATE
from players.STC.StcPlayer import StcPlayer

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

BAD_REWARD = -0.05

random.seed(1997)

FITTED_MODEL_GRID_SIZE = "6_1_opponent"


def get_reward(all_vertices_visited, timeout, not_visited, graph,scores:List[float]):
    reward = BAD_REWARD
    if all_vertices_visited:
        reward += 5 * scores[1]
    # elif timeout:
    #     return - GRID_SIZE ** 2
    if not_visited:
        reward += 1.0
    return reward


def simulate(graph_dimension_i, graph_dimension_j, players_list):
    iteration_number = 1
    graph = Graph2(graph_dimension_i, graph_dimension_j)
    num_of_robots = len(players_list)
    for player in players_list:
        player.set_graph(graph)
    scores = np.ones(num_of_robots)
    current_locations = [graph.get_random_cell() for _ in range(num_of_robots)]
    if current_locations[0]==current_locations[1]:
        scores[0]-=0.5
        scores[1]-=0.5
    for i, current_location in enumerate(current_locations):
        graph.set_visited(location=current_location, id=players_list[i].get_id())
    done = graph.all_vertices_visited()
    while not done:

        print(iteration_number) if (iteration_number % 100 == 0 and iteration_number > 0 and TEST_MODE) else None
        iteration_number += 1
        state = convert_data_to_state(current_locations[1],current_locations[0], graph)
        player_0_next_location = players_list[0].next_move(current_locations[0])
        player_1_next_location, action = players_list[1].next_move(current_locations[1], current_locations[0])
        TIMEOUT_THRESHOLD = 2000 if TEST_MODE else GRID_SIZE * 3 * 100
        timeout = (iteration_number > TIMEOUT_THRESHOLD)
        if player_1_next_location == current_locations[1]:
            reward = - 1.1 * graph.grid_size + BAD_REWARD
            done = True
            next_state = NOT_LEGAL_STATE
            players_list[1].dqn.push(Transition(state, action, reward, next_state, done))
            if TEST_MODE:
                done = timeout
                continue
            else:
                break
        not_visited = False
        next_locations = [player_0_next_location, player_1_next_location]

        if player_0_next_location == player_1_next_location and not graph.is_visited_by_any_robot(
                player_0_next_location):
            scores[0] += 0.5
            scores[1] += 0.5
            not_visited = True

        else:
            if not graph.is_visited_by_any_robot(next_locations[0]):
                scores[0] += 1
            if not graph.is_visited_by_any_robot(next_locations[1]):
                not_visited = True
                scores[1] += 1
        graph.set_visited(player_0_next_location, players_list[0].get_id())
        graph.set_visited(player_1_next_location, players_list[1].get_id())
        # print(next_locations)
        # print(scores)
        # graph.draw_graph(next_locations[1], next_locations[0])
        next_state = convert_data_to_state(player_1_next_location,player_0_next_location, graph)
        all_vertices_visited = graph.all_vertices_visited()
        done = all_vertices_visited or timeout
        reward = get_reward(all_vertices_visited, timeout, not_visited, graph, scores)
        players_list[1].dqn.push(Transition(state, action, reward, next_state, done))
        current_locations = next_locations
        if iteration_number % 5 == 0:
            players_list[1].dqn.update_model()
    return scores, iteration_number


if __name__ == "__main__":
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    model_file = 'rl-' + str(FITTED_MODEL_GRID_SIZE) + 'on' + str(FITTED_MODEL_GRID_SIZE) + '-model' + '.h5'
    if TEST_MODE:
        reconstructed_model = keras.models.load_model(model_file)
    else:
        reconstructed_model = None
    print("window size: " + str(WINDOW_SIZE) + " with grid size: " + str(GRID_SIZE) + " fitted: " + str(
        reconstructed_model is not None) + " of size: " + str(FITTED_MODEL_GRID_SIZE))
    results = []
    results_time = []
    results_steps = []
    averages = []
    averages_time = []
    averages_steps = []
    players_list = [StcPlayer(id=1), DqnPlayer(id=2, grid_size=GRID_SIZE, model=reconstructed_model)]
    i = 0
    number_of_runs = 100 if TEST_MODE else 750
    for i in range(0, number_of_runs):
        scores, number_of_iterations = simulate(GRID_SIZE, GRID_SIZE, players_list)
        print("Iteration number: " + str(i) + "  |||  Coverage is: " + str(scores))
        # print("Current iteration number: " + str(i) + " coverage is : " + str(scores[0])  + " number of total iterations: " + str(number_of_iterations))
        i += 1
        results.append(scores[1])
        results_steps.append(number_of_iterations)
        last_episodes = 100
        average_score1 = np.mean(results[-last_episodes:])
        average_score1_time = np.mean(results_time[-last_episodes:])
        average_score1_steps = np.mean(results_steps[-last_episodes:])

        averages += [average_score1]
        averages_time += [average_score1_time]
        averages_steps += [average_score1_steps]
        # if average_score1 == (GRID_SIZE ** 2) and not TEST_MODE:
        #     break
    print(averages_steps)
    if reconstructed_model is None and type(players_list[1]) is DqnPlayer:
        players_list[1].dqn.model.save(model_file)
    if not TEST_MODE:
        axes = plt.axes()
        axes.set_ylabel("average scores")
        axes.set_xlabel("epochs")
        plt.plot(averages)
        plt.title("Average score per 500 epochs")
        plt.show()

    axes = plt.axes()
    axes.set_ylabel("iterations scores")
    axes.set_xlabel("epochs")
    plt.plot(averages_steps)
    plt.title("Average iterations per 500 epochs")
    plt.show()
    import statistics

    print(statistics.mean(results_steps))
