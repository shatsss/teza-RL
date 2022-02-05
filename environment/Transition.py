class Transition:
    def __init__(self, state, action, reward, next_state, done):
        if next_state is None or state is None or action is None or reward is None or done is None:
            print("Shittttt")
        self.state = state
        self.action = action
        self.reward = reward
        self.next_state = next_state
        self.done = done
