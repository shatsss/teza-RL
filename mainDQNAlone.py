import os
import random
import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

from environment.Graph import Graph
from environment.Transition import Transition
from players.DQN.DQN import GRID_SIZE, WINDOW_SIZE, TEST_MODE
from players.DQN.DQNPlayerAlone import convert_data_to_state, NOT_LEGAL_STATE, DQNPlayerAlone

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

BAD_REWARD = -0.05

random.seed(1997)

# FITTED_MODEL_GRID_SIZE = "10_1_alone"
FITTED_MODEL_GRID_SIZE = "10_2_DQN_opponent_more_epochs"


def get_reward(all_vertices_visited, not_visited, graph):
    if all_vertices_visited:
        return 2.0 * graph.data[players_list[0].id].size
    elif not_visited:
        return 1.0
    else:
        return BAD_REWARD


def simulate(graph_dimension_i, graph_dimension_j, num_of_robots, players_list):
    iteration_number = 1
    start_time = time.process_time()
    graph = Graph(graph_dimension_i, graph_dimension_j)
    for player in players_list:
        player.set_graph(graph)
    scores = np.ones(num_of_robots)
    current_locations = [graph.get_random_cell() for _ in range(num_of_robots)]
    for i, current_location in enumerate(current_locations):
        graph.set_visited(location=current_location, id=players_list[i].id)
    done = graph.all_vertices_visited()
    while not done:
        # graph.draw_graph(current_locations[1], current_locations[0])
        print(iteration_number) if (iteration_number % 100 == 0 and iteration_number > 0 and TEST_MODE) else None
        state = convert_data_to_state(current_locations[0], graph)
        player_1_next_location, action = players_list[0].next_move(current_locations[0])
        TIMEOUT_THRESHOLD = 500 if TEST_MODE else 5000
        timeout = (iteration_number > TIMEOUT_THRESHOLD)
        if timeout:
            iteration_number = TIMEOUT_THRESHOLD
            break
        if player_1_next_location == current_locations[0]:
            reward = - 1.1 * graph.data[players_list[0].id].size
            done = True
            next_state = NOT_LEGAL_STATE
            if type(players_list[0]) is DQNPlayerAlone:
                players_list[0].dqn.push(Transition(state, action, reward, next_state, done))
                iteration_number = TIMEOUT_THRESHOLD

            break

        next_locations = [player_1_next_location]
        if not graph.is_visited(next_locations[0], players_list[0].id):
            scores[0] += 1
            not_visited = True
        else:
            not_visited = False
        graph.set_visited(player_1_next_location, players_list[0].id)
        next_state = convert_data_to_state(player_1_next_location, graph)
        all_vertices_visited = graph.all_vertices_visited()
        done = all_vertices_visited or timeout
        reward = get_reward(all_vertices_visited, not_visited, graph)
        if type(players_list[0]) is DQNPlayerAlone:
            players_list[0].dqn.push(Transition(state, action, reward, next_state, done))

        current_locations = next_locations
        if iteration_number % 10 == 0 and type(players_list[0]) is DQNPlayerAlone:
            players_list[0].dqn.update_model()
        iteration_number += 1

    return scores, time.process_time() - start_time, iteration_number


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
    players_list = [DQNPlayerAlone(id=2, model=reconstructed_model)]
    # players_list = [StcPlayer()]
    i = 0
    number_of_runs = 150 if TEST_MODE else 2500
    for i in range(0, number_of_runs):
        scores, total_time, number_of_iterations = simulate(GRID_SIZE, GRID_SIZE, 1, players_list)
        print("Current iteration number: " + str(i) + " coverage is : " + str(scores[0]) + " time: " + str(
            total_time) + " number of total iterations: " + str(number_of_iterations))
        i += 1
        results.append(scores[0])
        results_time.append(total_time)
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
    if reconstructed_model is None and type(players_list[0]) is DQNPlayerAlone:
        players_list[0].dqn.model.save(model_file)
    if not TEST_MODE:
        axes = plt.axes()
        axes.set_ylabel("average scores")
        axes.set_xlabel("epochs")
        plt.plot(averages)
        plt.title("Average score per 500 epochs")
        plt.show()

        axes = plt.axes()
        axes.set_ylabel("times scores")
        axes.set_xlabel("epochs")
        plt.plot(averages_time)
        plt.title("Average time per 500 epochs")
        plt.show()

    axes = plt.axes()
    axes.set_ylabel("iterations scores")
    axes.set_xlabel("epochs")
    plt.plot(averages_steps)
    plt.title("Average iterations per 500 epochs")
    plt.show()
    import statistics

    print(statistics.mean(results_steps))
