from random import choice
from typing import List
import matplotlib.pyplot as plt

# constant
GENERATIONS = 100
SIZE = 50

fig, ax = plt.subplots()

def create_map(size: int = SIZE) -> List[List[bool]]:
    """ Create a 2d map for given size """
    return [[choice([False, True]) for _ in range(size)] for _ in range(size)]


def show_map(map_: List[List[bool]]):
    """ Show the map in a readable form.
    :param map_: Array to show.
    """
    plt.ion()
    ax.clear()
    ax.imshow(map_, cmap='viridis')
    plt.draw()
    plt.pause(0.5)
    plt.ioff()


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
            count+=map_[x_pos][y_pos]
    return count


def update_map(old_map: List[List[bool]]) -> List[List[bool]]:
    """ Updates given map to next generation """
    new_map = old_map.copy()
    for x_coord, row in enumerate(old_map):
        for y_coord, _ in enumerate(row):
            alive_count = get_neighbours(old_map, x_coord, y_coord)
            if alive_count == 3:
                new_map[x_coord][y_coord] = True
            elif alive_count == 2 and old_map[x_coord][y_coord]:
                new_map[x_coord][y_coord] = True
            else:
                new_map[x_coord][y_coord] = False
    return new_map


if __name__ == '__main__':
    current_map = create_map()
    for iteration in range(GENERATIONS):
        print("iteration = ", iteration)
        current_map = update_map(current_map)
        show_map(current_map)
    plt.show()
