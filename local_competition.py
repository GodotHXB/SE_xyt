import random
import re
from settings import *
from ai import *


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


