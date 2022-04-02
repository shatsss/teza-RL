import random

import numpy as np
from tensorflow import keras

GRID_SIZE = 14
TEST_MODE = False

WINDOW_SIZE = 1


class DQN:

    def __init__(self, action_space_size, model=None):
        self.action_space_size = action_space_size
        self.min_epsilon = 0.0001
        if model is not None:
            self.model = model
            self.fitted_model = True
            self.epsilon = self.min_epsilon
        else:
            self.learning_rate = 0.001
            self.model = self.create_model(self.learning_rate)
            self.fitted_model = False
            self.epsilon = 1

        self.future_factory = 0.99
        self.batch_size = 256
        self.memory_size = 100000
        self.memory = []
        self.position = 0
        self.epsilon_decay = 0.9975

    def is_fitted(self):
        return self.fitted_model

    def create_model(self, lr):
        model = keras.Sequential()
        model.add(
            # keras.layers.Conv2D(4 * GRID_SIZE ** 2, (3, 3), padding='same',
            keras.layers.Conv2D(4 * (WINDOW_SIZE * 2 + 1) ** 2, (3, 3), padding='same',
                                input_shape=(WINDOW_SIZE * 2 + 1, WINDOW_SIZE * 2 + 1, 1)))
        # input_shape=(GRID_SIZE, GRID_SIZE, 1)))
        model.add(keras.layers.LeakyReLU(alpha=0.3))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(128))
        model.add(keras.layers.LeakyReLU(alpha=0.3))
        model.add(keras.layers.Dense(32))
        model.add(keras.layers.LeakyReLU(alpha=0.3))
        model.add(keras.layers.Dense(4, activation='linear'))

        optimizer = keras.optimizers.Adam(learning_rate=lr)
        model.compile(optimizer=optimizer, loss='mse', metrics=['mse'])
        return model

    def push(self, transition):
        # if self.is_fitted():
        #     return
        if len(self.memory) < self.memory_size:
            self.memory.append(None)
        self.memory[self.position] = transition
        self.position = (self.position + 1) % self.memory_size

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_space_size)
        expanded_state = np.expand_dims(state, axis=0)
        act_values = self.model.predict(expanded_state)
        return np.argmax(act_values[0])

    def update_model(self):
        # if self.is_fitted():
        #     return
        if self.epsilon > self.min_epsilon:
            self.epsilon *= self.epsilon_decay
        minibatch = random.choices(self.memory, k=self.batch_size)
        states = np.array([i.state for i in minibatch])
        actions = np.array([i.action for i in minibatch])
        rewards = np.array([i.reward for i in minibatch])
        next_states = np.array([i.next_state for i in minibatch])
        dones = np.array([i.done for i in minibatch])

        # states = np.squeeze(states)
        # next_states = np.squeeze(next_states)
        targets = rewards + self.future_factory * (np.amax(self.model.predict_on_batch(next_states), axis=1)) * (
                1 - dones)
        targets_full = np.array(self.model.predict_on_batch(states))
        for i in range(self.batch_size):
            targets_full[i][actions[i]] = targets[i]
        self.model.fit(states, targets_full, verbose=0)
