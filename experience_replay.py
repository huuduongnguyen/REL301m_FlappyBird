from collections import deque
import random

class ReplayMemory:
    def __init__(self, maxlen, seed=None):
        self.memory = deque([], maxlen=maxlen)
        if seed is not None:
            random.seed(seed)
    def append(self, transition):
        """Saves a transition."""
        self.memory.append(transition)

    def sample(self, sample_size):
        """Samples a batch of transitions."""
        return random.sample(self.memory, sample_size)

    def __len__(self):
        """Returns the current size of the memory."""
        return len(self.memory)