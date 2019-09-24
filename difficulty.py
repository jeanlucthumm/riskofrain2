import numpy as np

DRIZZLE = 1
RAINSTORM = 2
MONSOON = 3


def coeff(time, stage_time, player_count, diff_value):
    """
    Compute the difficulty coefficient
    :param time: array of increasing time values
    :param stage_time: average time spent per stage
    :param player_count: how many players are in the game
    :param diff_value: difficulty value {DRIZZLE|RAINSTORM|MONSOON}
    :return:
    """
    num_stages = np.floor_divide(time, stage_time)
    player_factor = 1 + 0.3 * (player_count - 1)
    time_factor = 0.046 * diff_value * player_count ** 2
    stage_factor = 1.15 ** num_stages
    return (player_factor + time * time_factor) * stage_factor


