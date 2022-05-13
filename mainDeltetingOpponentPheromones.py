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
from players.STC.StcPlayerWithDeletingPheromones import StcPlayerWithDeletingPheromones

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

BAD_REWARD = -0.5

random.seed(1997)
it_num = 2
# FITTED_MODEL_GRID_SIZE = "6_2_deleting_pheromones"
FITTED_MODEL_GRID_SIZE = "10_2_deleting_pheromones_grade_according_to_grid_size"


# FITTED_MODEL_GRID_SIZE = "14_2_DQN_opponent"


# FITTED_MODEL_GRID_SIZE = "10_1_alone"

def get_reward(all_vertices_visited, scores, visited_by_me_my_next_location, visited_by_opponent_my_next_location, grid_size):
    if all_vertices_visited:
        return 5.0 * scores[1]
    elif (not visited_by_me_my_next_location) and (not visited_by_opponent_my_next_location):
        return grid_size/5
    elif (not visited_by_opponent_my_next_location) and visited_by_me_my_next_location:
        return BAD_REWARD
    elif visited_by_opponent_my_next_location:
        return 1
    else:
        raise Exception("Error in calculating the reward value")


def simulate(graph_dimension_i, graph_dimension_j, players_list, it_num, should_draw=False):
    should_draw=True
    iteration_number = 1
    graph = Graph(graph_dimension_i, graph_dimension_j)
    for player in players_list:
        player.set_graph(graph)
    num_of_robots = len(players_list)
    scores = np.ones(num_of_robots)
    current_locations = [graph.get_random_cell() for _ in range(num_of_robots)]
    if current_locations[0] == current_locations[1]:
        scores -= 0.5
    for i, current_location in enumerate(current_locations):
        graph.set_visited(location=current_location, id=players_list[i].id)
    done = graph.all_vertices_visited()
    while not done:
        if should_draw:
            graph.draw_graph(current_locations[1], current_locations[0])
        print(iteration_number) if (iteration_number % 100 == 0 and iteration_number > 0 and TEST_MODE) else None
        iteration_number += 1
        state = convert_data_to_state(current_locations[1], current_locations[0], graph)
        player_0_next_location, _ = players_list[0].next_move(current_locations[0])
        # if type(player_0_next_location)==int:
        #     players_list[0].next_move(current_locations[0])
        player_1_next_location, action = players_list[1].next_move(current_locations[1], current_locations[0])
        TIMEOUT_THRESHOLD = 3000 if TEST_MODE else 5000
        timeout = (iteration_number > TIMEOUT_THRESHOLD)
        if timeout:
            break
        if player_1_next_location == current_locations[1]:
            reward = - 2 * graph.data[players_list[1].id].size
            done = True
            next_state = NOT_LEGAL_STATE
            if type(players_list[1]) is DQNPlayer:
                players_list[1].dqn.push(Transition(state, action, reward, next_state, done))
            if TEST_MODE:
                iteration_number = TIMEOUT_THRESHOLD
            break

        visited_by_me_my_next_location = True
        visited_by_opponent_my_next_location = True
        next_locations = [player_0_next_location, player_1_next_location]
        if player_0_next_location == player_1_next_location and not graph.is_visited_by_any_robot(
                player_0_next_location):
            scores[0] += 0.5
            scores[1] += 0.5
            visited_by_me_my_next_location = False
            visited_by_opponent_my_next_location = False
        else:
            if not graph.is_visited_by_any_robot(next_locations[0]):
                scores[0] += 1
            if not graph.is_visited_by_any_robot(next_locations[1]):
                scores[1] += 1
            visited_value_of_my_next_cell = graph.get_visited_value_of_cell(next_locations[1])
            if visited_value_of_my_next_cell == 1:
                visited_by_me_my_next_location = False
            elif visited_value_of_my_next_cell == 2:
                visited_by_opponent_my_next_location = False
            elif visited_value_of_my_next_cell == 7:
                visited_by_opponent_my_next_location = False
            elif visited_value_of_my_next_cell == 0:
                visited_by_opponent_my_next_location = False
                visited_by_me_my_next_location = False
            elif visited_value_of_my_next_cell == 3:
                pass
            else:
                raise Exception()
        if visited_by_opponent_my_next_location:
            graph.delete_opponent_pheromone(location=player_1_next_location, id=players_list[0].get_id())
        graph.set_visited(player_0_next_location, players_list[0].get_id())
        graph.set_visited(player_1_next_location, players_list[1].get_id())
        next_state = convert_data_to_state(player_1_next_location, player_0_next_location, graph)
        all_vertices_visited = graph.all_vertices_visited()
        done = all_vertices_visited
        reward = get_reward(all_vertices_visited, scores, visited_by_me_my_next_location,
                            visited_by_opponent_my_next_location, grid_size=graph.grid_size)
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
    players_list = [StcPlayerWithDeletingPheromones(id=1), DQNPlayer(id=2, model=reconstructed_model)]
    # players_list = [StcPlayer(id=1)]
    i = 0
    number_of_wins = 0
    number_of_draws = 0
    number_of_loses = 0
    number_of_runs = 500 if TEST_MODE else 5000
    for i in range(0, number_of_runs):
        if i > number_of_runs:
            should_draw = True
        else:
            should_draw = False
        scores, it_num, number_of_iterations = simulate(GRID_SIZE, GRID_SIZE, players_list, it_num,
                                                        should_draw=should_draw)
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

    # print(statistics.mean(results_steps))
    # print("epsilon : " + str(players_list[1].dqn.epsilon))
    print("Number of wins: " + str(number_of_wins / number_of_runs))
    print("Number of loses: " + str(number_of_loses / number_of_runs))
    print("Number of draws: " + str(number_of_draws / number_of_runs))
