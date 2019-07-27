from math import inf
from random import randint

TOTAL_PLAYERS = 4


def _roll_die():
    return randint(1, 6)


def _roll_dice(n):
    r = 0
    for i in range(n):
        r += _roll_die()
    return r


def _player_input():
    r = input('How many tools?')
    return r


class _BoardSpace:
    def __init__(self, meeple_min=1, meeple_max=inf, max_players=inf, resolution=None, divisor=None, resource=None):
        self.meeple_min = meeple_min
        self.meeple_max = meeple_max
        self.max_players = max_players
        self.current_meeples = {}
        self.resolution = resolution
        self.divisor = divisor
        self.resource = resource

    def place(self, player_nm, meeples):
        if len(self.current_meeples) >= self.max_players:
            print("No more players can place meeples")

        elif player_nm in self.current_meeples.keys():
            print(f"Player {player_nm} has already placed meeples")

        elif not self.meeple_min <= (meeples + sum(self.current_meeples.values())) <= self.meeple_max:
            print(f"Not enough spaces for {meeples} meeples")

        else:
            self.current_meeples[player_nm] = meeples

    def resolve(self, player):
        # TODO: Replace this with a dict
        if self.resolution == 'resources':
            self.resolve_gathering(player)
        elif self.resolution == 'village':
            pass
        elif self.resolution == 'purchase':
            pass

    def resolve_gathering(self, player):
        if player.player_nm not in self.current_meeples.keys():
            f"Player {player.player_nm} does not have meeples here"
        dice_result = _roll_dice(self.current_meeples.pop(player.player_nm))
        if len(player.available_tools) > 0:
            # TODO: Need to expand this
            dice_result += _player_input()
        print(player.player_nm, dice_result)
        player.resources[self.resource] += dice_result // self.divisor


class Player:
    def __init__(self, player_nm):
        self.player_nm = player_nm

        self.meeples = 5
        self.ag_level = 0
        # TODO: Need method to increment this, and enforce list.
        self.tools = []
        # TODO: Need method to set/reset each round
        # TODO: Need to address temp tools
        self.available_tools = []

        self.cards = []
        self.buildings = []
        self.resources = {
            'food': 10,
            'wood': 0,
            'clay': 0,
            'stone': 0,
            'gold': 0
        }

    def place_people(self, location, meeples):
        location.place(self.player_nm, meeples)


class NewGame:
    def __init__(self, player_ct):
        self.game_board = _Board
        self.players = []
        for i in range(player_ct):
            # TOOD: Abstract input for AI play
            nm = input(f"Input player #{i+1}'s name: ")
            self.players.append(Player(nm))

    def play(self):
        # Phase 1 - Players place people
        # Phase 2 - Players resolve people
        # Phase 3 - Feed meeples
        pass

    def resolve_player(self, player, board):
        # TODO: Add scan for meeples
        board.forest.resolution()


class _Board:
    def __init__(self):
        mp = self._max_gatherers()
        self.hunting = _BoardSpace(meeple_max=inf, max_players=inf, resolution='resources', divisor=2, resource='food')
        self.forest = _BoardSpace(meeple_max=7, max_players=mp, resolution='resources', divisor=3, resource='wood')
        self.mound = _BoardSpace(meeple_max=7, max_players=mp, resolution='resources', divisor=4, resource='clay')
        self.quarry = _BoardSpace(meeple_max=7, max_players=mp, resolution='resources', divisor=5, resource='stone')
        self.river = _BoardSpace(meeple_max=7, max_players=mp, resolution='resources', divisor=6, resource='gold')

    def _max_gatherers(self):
        if TOTAL_PLAYERS < 4:
            self.max_players = TOTAL_PLAYERS - 1
        else:
            self.max_players = TOTAL_PLAYERS
        return self.max_players


if __name__ == '__main__':
    game = NewGame(4)
    for player in game.players:
        print(vars(player))
    # p1 = Player('Matt')
    # p2 = Player('Anne')
    # p3 = Player('Sarah')
    # p4 = Player('Chris')

    # p1.place_people(board.forest, 2)
    # p2.place_people(board.forest, 3)
    # p3.place_people(board.forest, 2)
    #
    # print(board.forest.current_meeples)
    # board.forest.resolve(p1)
    # print(p1.resources)
    #
    # print(board.forest.current_meeples)
    # board.forest.resolve(p2)
    # print(p2.resources)
    #
