from Checker import Checker
from Pos import Pos
def pop_strategy(game):
    try:
        p = game.get_board().get_oppcells()[0].get_checker()
    except:
        p = Pos(0, 0).get_checker()

    return game.pop(p)


