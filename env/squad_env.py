import numpy as np

class SquadTrainingEnv:
    """
    A simplified training environment for reinforcement learning.
    State:
        [fitness (0-100), marksmanship (0-100), fatigue (0-100)]

    Actions:
        0 = Physical Training
        1 = Shooting Training
        2 = Tactical Exercise
        3 = Rest
    """

    def __init__(self):
        self.reset()

    def reset(self):
        self.fitness = 55
        self.marksmanship = 55
        self.fatigue = 20
        return self._state()

    def _state(self):
        return np.array([self.fitness, self.marksmanship, self.fatigue], dtype=float)

    def step(self, action):
        fitness_gain, mark_gain, fatigue_gain = 0, 0, 0

        if action == 0:  # Physical
            fitness_gain = np.random.uniform(1, 3)
            fatigue_gain = 5

        elif action == 1:  # Shooting
            mark_gain = np.random.uniform(1, 2.5)
            fatigue_gain = 4

        elif action == 2:  # Tactics
            fitness_gain = np.random.uniform(0.5, 1.5)
            mark_gain = np.random.uniform(0.5, 1.2)
            fatigue_gain = 6

        elif action == 3:  # Rest
            fatigue_gain = -6

        # apply updates
        self.fitness = np.clip(self.fitness + fitness_gain, 0, 100)
        self.marksmanship = np.clip(self.marksmanship + mark_gain, 0, 100)
        self.fatigue = np.clip(self.fatigue + fatigue_gain, 0, 100)

        # reward = overall performance gain - fatigue penalty
        reward = (fitness_gain + mark_gain) - max(0, fatigue_gain * 0.4)

        done = self.fatigue >= 100 or (self.fitness >= 95 and self.marksmanship >= 95)

        return self._state(), reward, done
