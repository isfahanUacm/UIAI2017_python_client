from Pos import Pos
from Checker import Checker
def move_strategy(game):
    import random
    l = list(range(len(game.get_board().get_mycells())))
    random.shuffle(l)
    for i in l:
        cell = game.get_board().get_mycells()[i]
        l2 = list(range(len(game.get_board().get_neighbors(cell))))
        random.shuffle(l2)
        for j in l2:
            n  = game.get_board().get_neighbors(cell)[j]
            if n.get_checker() is None:
                game.move(cell,n.get_pos())
