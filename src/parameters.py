import json

from simulated_world import Shape


def get_parameters():
    parameters = Parameters()
    with open('src/pivotal_parameters.json', 'r') as f:
        pivotal_parameters = json.load(f)
        for attr, value in pivotal_parameters.items():
            setattr(parameters, attr, value)
        if parameters.board_type == 1:
            parameters.board_type = Shape.Diamond
        else:
            parameters.board_type = Shape.Triangle
    return parameters


class Parameters:

    episodes: int
    visualize_games: bool

    # Simulated World
    board_type: Shape
    size: int
    holes: list

    # Actor
    actor_learning_rate: float
    actor_trace_decay: float
    actor_discount_factor: float
    actor_epsilon: float
    actor_epsilon_decay_rate: float
    actor_nn_dimensions: tuple

    # Critic
    critic_learning_rate: float
    critic_trace_decay: float
    critic_discount_factor: float
    critic_nn_dimensions: tuple