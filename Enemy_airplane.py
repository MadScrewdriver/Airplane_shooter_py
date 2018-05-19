
class Enemy(object):

    def __init__(self, game, player, bullets):
        self.game = game
        self.player = player
        self.enemies = []
        self.size = self.game.screen.get_size()

        self.mask = {
            "mask1": {

                "x1": 1

            }
        }