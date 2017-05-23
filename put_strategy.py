from Pos import Pos
def put_strategy(game):
    try:
        p = game.get_board().get_emptycells()[0].get_pos()
    except:
        p = Pos(0, 0)

    return game.put(p)


