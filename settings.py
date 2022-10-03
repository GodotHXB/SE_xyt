import random


class Board:
    # 棋盘类
    def __init__(self, pos, count):
        self.pos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.count = 0


class Player:
    # 玩家类
    def __init__(self,score,figure):
        self.score = 0
        self.figure = 0


def game_status(board_A,board_B):
    # 判定游戏是否结束
    if board_A.count == 9 or board_B.count == 9:
        return False
    else:
        return True
