from Checker import Checker
from Pos import Pos
def pop_strategy(game):
    p = game.get_board().get_oppcells()[0].get_checker()
    game.pop(p)


