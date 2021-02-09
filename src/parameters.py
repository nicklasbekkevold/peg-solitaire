from data_classes import Shape

# General
EPISODES = 500
VISUALIZE_GAMES = False
FRAME_DELAY = 0.3

# Simulated World
BOARD_TYPE = Shape.Diamond
SIZE = 5
HOLES = set([
    (3, 2),
])

# Actor
ACTOR_LEARNING_RATE = 0.1
ACTOR_DISCOUNT_FACTOR = 0.9999
ACTOR_TRACE_DECAY = 0.9999
ACTOR_EPSILON = 1.0
ACTOR_EPSILON_DECAY = 0.9999

# Critic
USE_TABLE_CRITIC = False
CRITIC_LEARNING_RATE = 0.1
CRITIC_DISCOUNT_FACTOR = 0.9999
CRITIC_TRACE_DECAY = 0.9999
CRITIC_NN_DIMENSIONS = (16, 20, 30, 5, 1)
