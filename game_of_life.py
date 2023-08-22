from pprint import pprint
from random import choice
from typing import List

# constant
GENERATIONS = 10


def create_map(size: int = 5) -> List[List[bool]]:
    """Create a 2d map for given size
    [
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ]

    """
    # map_ = []
    # for _ in range(size):
    #     row = []
    #     for _ in range(size):
    #         row.append(choice([False, True]))
    #     map_.append(row)
    #
    # return map_
    return [[choice([False, True]) for _ in range(size)] for _ in range(size)]


def show_map(map_: List[List[bool]]):
    """ Show the map in a readable form.
    :param map_: Array to show.
    """
    # matplotlib library.. google how to do 2d animation.
    pprint(map_)


def get_neighbours(map_: List[List[bool]], coordinate_row: int, coordinate_column: int) -> int:
    """ Get the number of neighbours with the value True.
    :param map_: Array.
    :param coordinate_row: row position.
    :param coordinate_column: column position.
    :return: the number of neighbours with the value True.
    """
    count = 0
    for x_pos in range(coordinate_row - 1, coordinate_row + 2):
        for y_pos in range(coordinate_column - 1, coordinate_column + 2):
            if x_pos < 0 or y_pos < 0:
                continue
            if x_pos == coordinate_row and y_pos == coordinate_column:
                continue
            if x_pos >= len(map_) or y_pos >= len(map_):
                continue
            if map_[x_pos][y_pos] is True:
                count+=1
    return count


def update_map(old_map: List[List[bool]]) -> List[List[bool]]:
    """ Updates given map to next generation """
    # HOMEWORK
    # we iterate over whole map
    # check number of alive neighbours
    # decision: live or die
    # return updated/new map
    new_map = old_map.copy()
    for x_coord, row in enumerate(old_map):
        for y_coord, value in enumerate(row):
            alive = get_neighbours(old_map, x_coord, y_coord)
            if alive < 2 or alive > 3:
                new_map[x_coord][y_coord] = False
            if alive == 3:
                new_map[x_coord][y_coord] = True
            if alive == 2 and old_map[x_coord][y_coord] is True:
                new_map[x_coord][y_coord] = True
    show_map(new_map)
    return new_map


def recursive(times, map_):
    """ 
    """
    if times == 1:
        update_map(map_)
    else:
        map__ = update_map(map_)
        recursive(times - 1, map__)


if __name__ == '__main__':
    current_map = create_map()
    show_map(current_map)
    sec_map = update_map(current_map)
    #recursive(GENERATIONS, sec_map)
