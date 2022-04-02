import os
import random
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

from environment.Graph import Graph
from environment.Transition import Transition
from players.DQN.DQN import GRID_SIZE, WINDOW_SIZE, TEST_MODE
from players.DQN.DqnPlayer import convert_data_to_state, NOT_LEGAL_STATE, DQNPlayer
from players.STC.StcPlayer import StcPlayer

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

BAD_REWARD = -0.05

random.seed(1997)
it_num = 2
# FITTED_MODEL_GRID_SIZE = "14_1_DQN_opponent_same_pheromones"
# FITTED_MODEL_GRID_SIZE = "14_1_DQN_opponent"


FITTED_MODEL_GRID_SIZE = "14_1_alone"

def get_reward(all_vertices_visited, not_visited, scores):
    if all_vertices_visited:
        return 2.0 * scores[1]
    elif not_visited:
        return 1.0
    else:
        return BAD_REWARD


def simulate(graph_dimension_i, graph_dimension_j, players_list, it_num):
    iteration_number = 1
    graph = Graph(graph_dimension_i, graph_dimension_j)
    for player in players_list:
        player.set_graph(graph)
    num_of_robots = len(players_list)
    scores = np.ones(num_of_robots)
    current_locations = [graph.get_random_cell() for _ in range(num_of_robots)]
    for i, current_location in enumerate(current_locations):
        graph.set_visited(location=current_location, id=players_list[i].id)
    done = graph.all_vertices_visited()
    while not done:
        # graph.draw_graph(current_locations[1], current_locations[0])
        print(iteration_number) if (iteration_number % 100 == 0 and iteration_number > 0 and TEST_MODE) else None
        iteration_number += 1
        state = convert_data_to_state(current_locations[1], current_locations[0], graph)
        player_0_next_location, _ = players_list[0].next_move(current_locations[0])
        player_1_next_location, action = players_list[1].next_move(current_locations[1], current_locations[0])
        TIMEOUT_THRESHOLD = 500 if TEST_MODE else 5000
        timeout = (iteration_number > TIMEOUT_THRESHOLD)
        if timeout:
            break
        if player_1_next_location == current_locations[1]:
            reward = - 1.1 * graph.data[players_list[1].id].size
            done = True
            next_state = NOT_LEGAL_STATE
            if type(players_list[1]) is DQNPlayer:
                players_list[1].dqn.push(Transition(state, action, reward, next_state, done))
            if TEST_MODE:
                iteration_number = TIMEOUT_THRESHOLD
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
                scores[1] += 1
                not_visited = True
        graph.set_visited(player_0_next_location, players_list[0].get_id())
        graph.set_visited(player_1_next_location, players_list[1].get_id())
        next_state = convert_data_to_state(player_1_next_location, player_0_next_location, graph)
        all_vertices_visited = graph.all_vertices_visited()
        done = all_vertices_visited
        reward = get_reward(all_vertices_visited, not_visited, scores)
        # if timeout:
        #     print("Timeout!!!")
        if type(players_list[1]) is DQNPlayer:
            players_list[1].dqn.push(Transition(state, action, reward, next_state, done))
        current_locations = next_locations
        if it_num % 10 == 0 and type(players_list[1]) is DQNPlayer:
            players_list[1].dqn.update_model()
        it_num += 1
    return scores, it_num, iteration_number


if __name__ == "__main__":
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("without opponent location in the state")
    print("Current Time =", current_time)
    model_file = 'rl-' + str(FITTED_MODEL_GRID_SIZE) + 'on' + str(FITTED_MODEL_GRID_SIZE) + '-model' + '.h5'
    if TEST_MODE:
        reconstructed_model = keras.models.load_model(model_file)
    else:
        reconstructed_model = None
    # reconstructed_model=None
    print("window size: " + str(WINDOW_SIZE) + " with grid size: " + str(GRID_SIZE) + " fitted: " + str(
        reconstructed_model is not None) + " of size: " + str(FITTED_MODEL_GRID_SIZE))
    results = []
    results_steps = []
    averages = []
    averages_steps = []
    players_list = [StcPlayer(id=1), DQNPlayer(id=2, model=reconstructed_model)]
    # players_list = [StcPlayer(id=1)]
    i = 0
    number_of_wins = 0
    number_of_draws = 0
    number_of_loses = 0
    number_of_runs = 1000 if TEST_MODE else 7500
    for i in range(0, number_of_runs):
        scores, it_num, number_of_iterations = simulate(GRID_SIZE, GRID_SIZE, players_list, it_num)
        print("Current iteration number: " + str(i) + " coverage is : " + str(scores[1]) + " opponent coverage: " + str(
            scores[0]) + " number of total iterations: " + str(number_of_iterations))
        if scores[0] < scores[1]:
            number_of_wins += 1
        elif scores[0] > scores[1]:
            number_of_loses += 1
        else:
            number_of_draws += 1
        i += 1
        results.append(scores[1])
        results_steps.append(number_of_iterations)
        last_episodes = 100
        average_score1 = np.mean(results[-last_episodes:])
        average_score1_steps = np.mean(results_steps[-last_episodes:])

        averages += [average_score1]
        averages_steps += [average_score1_steps]
        # if average_score1 == (GRID_SIZE ** 2) and not TEST_MODE:
        #     break
    # print(averages_steps)
    if reconstructed_model is None and type(players_list[1]) is DQNPlayer:
        players_list[1].dqn.model.save(model_file)
    if TEST_MODE:
        axes = plt.axes()
        axes.set_ylabel("average scores")
        axes.set_xlabel("epochs")
        plt.plot(averages)
        plt.title("Average score per 500 epochs")
        plt.show()
    else:
        axes = plt.axes()
        axes.set_ylabel("iterations scores")
        axes.set_xlabel("epochs")
        plt.plot(averages_steps)
        plt.title("Average iterations per 500 epochs")
        plt.show()
        import statistics

    # print(statistics.mean(results_steps))
    # print("epsilon : " + str(players_list[1].dqn.epsilon))
    print ("Number of wins: " + str(number_of_wins/number_of_runs))
    print ("Number of loses: " + str(number_of_loses/number_of_runs))
    print ("Number of draws: " + str(number_of_draws/number_of_runs))

