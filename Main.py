from Game import Game

if __name__ == '__main__':
    game = Game("127.0.0.1", 9999, "team2")
    if game.start_client():
        game.start()

