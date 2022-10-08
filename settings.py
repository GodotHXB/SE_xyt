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

def score_process(board_A, board_B, start, end, score_A, score_B):
    # 按行结算分数
    countA = [0,0,0,0,0,0,0]
    countB = [0,0,0,0,0,0,0]
    # 记录每个数字出现的次数
    for i in range(start,end):
        countA[board_A.pos[i]] += 1
        countB[board_B.pos[i]] += 1
    # 按点数1-6的顺序计算分数
    for i in range(1,7):
        score_A += (i * countA[i] ** 2)
        score_B += (i * countB[i] ** 2)
    return score_A,score_B


def print_board(board_A,board_B):
    # 打印棋盘
    print("A方棋盘如下：            B方棋盘如下：")
    count = 0
    for i in range(0,9):
        print(board_A.pos[i],end='\t')
        count = count + 1
        if count == 3:
            print('           ',end='')
            for j in range(i-2,i+1):
                print(board_B.pos[j],end='\t')
            count = 0
            print('\n')


def end_game(board_A, board_B):
    # 计算总分
    score_A = 0
    score_B = 0

    score_A,score_B = score_process(board_A,board_B,0,3,score_A,score_B)
    score_A,score_B = score_process(board_A,board_B,3,6,score_A,score_B)
    score_A,score_B = score_process(board_A,board_B,6,9,score_A,score_B)

    print("A的得分为: ", score_A)
    print("B的得分为: ", score_B)

    if score_A > score_B:
        print("A获胜！")
    elif score_A < score_B:
        print("B获胜！")
    else:
        print("平局！")


def remove_figure(index,figure,opposite):
    # 消除对手的骰子
    if 0 <= index < 3:
        for i in range(0,3):
            if opposite.pos[i] == figure:
                opposite.pos[i] = 0
                opposite.count -= 1

    if 3 <= index < 6:
        for i in range(3,6):
            if opposite.pos[i] == figure:
                opposite.pos[i] = 0
                opposite.count -= 1

    if 6 <= index < 9:
        for i in range(6,9):
            if opposite.pos[i] == figure:
                opposite.pos[i] = 0
                opposite.count -= 1