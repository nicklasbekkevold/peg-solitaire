from data_classes import Shape

# General
EPISODES = 175
VISUALIZE_GAMES = False
FRAME_DELAY = 0.15

# Simulated World
BOARD_TYPE = Shape.Diamond
SIZE = 4
HOLES = set([
    # (1, 1), Not solvable
    (1, 2),  # C_a
    # (2, 1),  # C_b
    # (2, 2), Not solvable
])
WINNING_REWARD = 10
LOSING_REWARD = -1
STEP_REWARD = 0

# Actor
ACTOR_LEARNING_RATE = 0.001
ACTOR_DISCOUNT_FACTOR = 0.92
ACTOR_TRACE_DECAY = 0.9

ACTOR_EPSILON = 1
ACTOR_EPSILON_DECAY = 0.994

# Critic
CRITIC_LEARNING_RATE = 0.0001
CRITIC_DISCOUNT_FACTOR = 0.92
CRITIC_TRACE_DECAY = 0.9

USE_TABLE_CRITIC = False
INPUT_DIMENSION = SIZE ** 2 if BOARD_TYPE == Shape.Diamond else int((SIZE * (SIZE + 1)) / 2)
CRITIC_NN_DIMENSIONS = (INPUT_DIMENSION, 20, 30, 5, 1)
