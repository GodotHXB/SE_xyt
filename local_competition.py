import random
import re
from settings import *
from ai import *


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


def start_game_local():
    # 初始化
    player_A = Player(0, 0)
    player_B = Player(0, 0)
    board_A = Board([], 0)
    board_B = Board([], 0)

    # player_A先手
    while game_status(board_A, board_B):
        num = random.randint(1,6)
        print_board(board_A,board_B)
        print('A方得到的数字为：',num)

        index = input("请输入想放置的位置（1-3第一行，4-6第二行，7-9第三行）：")
        while not re.findall('[1-9]',index):
            index = input("请输入正确的数字（1-3第一行，4-6第二行，7-9第三行）：")
        index = int(index)

        while board_A.pos[index-1] != 0:
            print("该位置已放置骰子，请重新选择放置位置：")
            index = int(input("请输入想放置的位置（1-3第一行，4-6第二行，7-9第三行）："))

        board_A.pos[index-1] = num
        board_A.count += 1
        remove_figure(index-1,num,board_B)

        if (game_status(board_A, board_B) == False):
            break

        # 轮到B出手
        num = random.randint(1, 6)
        print_board(board_A, board_B)
        print('B方得到的数字为：', num)

        index = input("请输入想放置的位置（1-3第一行，4-6第二行，7-9第三行）：")
        while not re.findall('[1-9]',index):
            index = input("请输入正确的数字（1-3第一行，4-6第二行，7-9第三行）：")
        index = int(index)

        while board_B.pos[index-1] != 0:
            print("该位置已放置骰子，请重新选择放置位置：")
            index = int(input("请输入想放置的位置（1-3第一行，4-6第二行，7-9第三行）："))

        board_B.pos[index-1] = num
        board_B.count += 1
        remove_figure(index-1,num,board_A)

    end_game(board_A,board_B)


def start_game_ai():
    # 初始化
    player_A = Player(0, 0)
    player_B = Player(0, 0)
    board_A = Board([], 0)
    board_B = Board([], 0)


    while game_status(board_A, board_B):
        #我方先手
        num = random.randint(1,6)
        print_board(board_A,board_B)
        print('A方得到的数字为：',num)

        index = input("请输入想放置的位置（1-3第一行，4-6第二行，7-9第三行）：")
        while not re.findall('[1-9]',index):
            index = input("请输入正确的数字（1-3第一行，4-6第二行，7-9第三行）：")
        index = int(index)

        while board_A.pos[index-1] != 0:
            print("该位置已放置骰子，请重新选择放置位置：")
            index = int(input("请输入想放置的位置（1-3第一行，4-6第二行，7-9第三行）："))

        board_A.pos[index-1] = num
        board_A.count += 1
        remove_figure(index-1,num,board_B)

        if (game_status(board_A, board_B) == False):
            break

        # 轮到AI出手
        num = random.randint(1, 6)
        # print_board(board_A, board_B)
        print('B方得到的数字为：', num)

        index = nextStep(board_B.pos,board_A.pos,num)

        # 此处index为真实位置的索引，无需减1
        board_B.pos[index] = num
        board_B.count += 1
        remove_figure(index,num,board_A)

    end_game(board_A,board_B)


if __name__ == '__main__':
    # print_board(board_test,board_test1)
    pass


