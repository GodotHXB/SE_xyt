import random


def calculate_row(ownBoard, otherBoard,start,end,figure):
    count_own = [0,0,0,0,0,0,0] # ownBoard上某行某个数字出现的次数
    count_other = [0,0,0,0,0,0,0] # otherBoard上某行某个数字出现的次数

    for i in range(start, end):
        count_own[ownBoard[i]] += 1
        count_other[otherBoard[i]] += 1
    for i in range(1, 7):
        score = figure * count_other[figure] ** 2 + figure * (count_own[figure] + 1) ** 2
    return score


def place_dice(ownBoard,start,end):
    index = -1
    for i in range(start, end):
        if ownBoard[i] == 0:
            index = i
            break
    return index


def nextStep(ownBoard,otherBoard,figure):
    # 初始化，用于记录数值
    k_score = 0 # 放置在k行取得的净胜分
    e_score = 0 # 放置在e行取得的净胜分
    x_score = 0 # 放置在x行取得的净胜分
    index = -1

    # 处理K线
    k_score = calculate_row(ownBoard, otherBoard, 0, 3, figure)
    e_score = calculate_row(ownBoard, otherBoard, 3, 6, figure)
    x_score = calculate_row(ownBoard, otherBoard, 6, 9, figure)
    # print('k_score = ', k_score,',e_score = ', e_score,',x_score = ',x_score)

    # 建立dict，按照value值对净胜分进行排序，由高到低进行选择
    scores = {'k':k_score,'e':e_score,'x':x_score}
    scores_list = sorted(scores.items(), key=lambda s: s[1], reverse=True)
    # print(scores_list)

    for score in scores_list:
        if score[0] == 'k':
            index = place_dice(ownBoard, 0, 3)
        elif score[0] == 'e':
            index = place_dice(ownBoard, 3, 6)
        elif score[0] == 'x':
            index = place_dice(ownBoard, 6, 9)
        # 找到最优位置，中止循环
        if index != -1:
            break

    return index