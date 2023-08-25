from game_of_life import get_neighbours

def test_get_neighbours_positive():
    map_ = [[True,False,False],
            [True,True,True],
            [False,True,False]
            ]
    dict_ = {(0,0):2,(0,1):4,(0,2):2,(1,0):3,(1,1):4,(1,2):2,(2,0):3,(2,1):3,(2,2):3}
    for coord, value in dict_.items():
        neighbours = get_neighbours(map_, coord[0], coord[1])
        assert neighbours == value, f"Incorect number of neighbours. {coord}"

