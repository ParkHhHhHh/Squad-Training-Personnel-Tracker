import numpy as np
from collections import defaultdict

class QLearningAgent:
    def __init__(self, action_size=4, lr=0.1, gamma=0.95, epsilon=0.2):
        self.action_size = action_size
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon

        # Q-table: state will be discretized for simplicity
        self.Q = defaultdict(lambda: np.zeros(action_size))

    def discretize(self, state):
        return tuple((state // 10).astype(int))  # reduce complexity

    def get_action(self, state):
        s = self.discretize(state)

        if np.random.rand() < self.epsilon:
            return np.random.randint(self.action_size)

        return np.argmax(self.Q[s])

    def update(self, state, action, reward, next_state):
        s = self.discretize(state)
        ns = self.discretize(next_state)

        best_next = np.max(self.Q[ns])
        td_error = reward + self.gamma * best_next - self.Q[s][action]

        self.Q[s][action] += self.lr * td_error
