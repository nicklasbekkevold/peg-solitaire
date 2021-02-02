from typing import Tuple
from data_classes import Shape

# General
EPISODES = int(500)
VISUALIZE_GAMES = bool(False)
FRAME_DELAY = 0.3

# Simulated World
BOARD_TYPE = Shape(Shape.Diamond)
SIZE = 5
HOLES: Tuple[Tuple[int, int]] = tuple([
    (0, 1),
    (2, 1),
])

# Actor
ACTOR_LEARNING_RATE = 0.1
ACTOR_DISCOUNT_FACTOR = 0.9
ACTOR_TRACE_DECAY = 0.8
ACTOR_EPSILON = 0.5
ACTOR_EPSILON_DECAY = 0.9

# Critic
USE_TABLE_CRITIC = bool(True)
CRITIC_LEARNING_RATE = 0.001
CRITIC_DISCOUNT_FACTOR = 0.9
CRITIC_TRACE_DECAY = 0.8
CRITIC_NN_DIMENSIONS: Tuple[int, ...] = (15, 20, 30, 5, 1)
