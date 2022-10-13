import random

def score_process(ownBoard, otherBoard, start, end, own_score, other_score):
    # 按行结算分数
    countA = [0,0,0,0,0,0,0]
    countB = [0,0,0,0,0,0,0]
    # 记录每个数字出现的次数
    for i in range(start,end):
        countA[ownBoard[i]] += 1
        countB[otherBoard[i]] += 1
    # 按点数1-6的顺序计算分数
    for i in range(1,7):
        own_score += (i * countA[i] ** 2)
        other_score += (i * countB[i] ** 2)
    return own_score,other_score


def calculate_row(ownBoard, otherBoard, start, end, figure, type='greedy'):
    # 计算我方某行得分与某行已放置的骰子数
    # 最后一个参数type代表决策类型，greedy = 贪婪， conservative = 保守
    count_own = [0,0,0,0,0,0,0] # ownBoard上某行某个数字出现的次数
    count_other = [0,0,0,0,0,0,0] # otherBoard上某行某个数字出现的次数
    count = 0

    for i in range(start, end):
        count_own[ownBoard[i]] += 1
        count_other[otherBoard[i]] += 1

    if type == 'greedy':
            score = figure * count_other[figure] ** 2 + figure * (count_own[figure] + 1) ** 2 # 消除对面的

    elif type == 'conservative':
        if count_other[figure] != 0:
            score = -1 # 如果对面该行有此数字，最差解
        else:
            score = figure * (count_own[figure] + 1) ** 2 # 不消对面的

    count = 3 - count_own[0] # 算骰子数
    return score,count


def calculate_all(ownBoard,otherBoard):
    # 计算当前双方总分数
    own_score = 0
    other_score = 0

    own_score, other_score = score_process(ownBoard, otherBoard, 0, 3, own_score, other_score)
    own_score, other_score = score_process(ownBoard, otherBoard, 3, 6, own_score, other_score)
    own_score, other_score = score_process(ownBoard, otherBoard, 6, 9, own_score, other_score)

    return own_score,other_score


def place_dice(ownBoard,start,end):
    # 放置骰子
    index = -1
    for i in range(start, end):
        if ownBoard[i] == 0:
            index = i
            break
    return index


def nextStep(ownBoard,otherBoard,figure):
    # 最终版本
    index = -1 # 要返回的放置位置，初始置-1
    # 初始化，用于记录数值
    k_score = 0 # 放置在k行取得的净胜分
    e_score = 0 # 放置在e行取得的净胜分
    x_score = 0 # 放置在x行取得的净胜分
    k_count = 0 # 放置在k行的骰子数
    e_count = 0 # 放置在e行的骰子数
    x_count = 0 # 放置在x行的骰子数
    own_score, other_score = calculate_all(ownBoard,otherBoard)
    # print(own_score,other_score)

    if own_score - other_score >= 60: # 分差达到60时代表优势很大，可视作这把比赛必赢，应尽快结束比赛
        # 处理K线
        k_score,k_count = calculate_row(ownBoard, otherBoard, 0, 3, figure, 'conservative')
        e_score,e_count = calculate_row(ownBoard, otherBoard, 3, 6, figure, 'conservative')
        x_score,x_count = calculate_row(ownBoard, otherBoard, 6, 9, figure, 'conservative')
        # print('k_score = ', k_score,',e_score = ', e_score,',x_score = ',x_score)

        scores = {'k':[k_score,k_count],'e':[e_score,e_count],'x':[x_score,x_count]}
        scores_list = sorted(scores.items(), key=lambda s: (s[1][0],-s[1][1]), reverse=True)# 优先分数高，相等时放空位最多的行
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

    else: # 优势不大，继续贪
        # 处理K线
        k_score,k_count = calculate_row(ownBoard, otherBoard, 0, 3, figure)
        e_score,e_count = calculate_row(ownBoard, otherBoard, 3, 6, figure)
        x_score,x_count = calculate_row(ownBoard, otherBoard, 6, 9, figure)
        # print('k_score = ', k_score,',e_score = ', e_score,',x_score = ',x_score)

        scores = {'k':[k_score,k_count],'e':[e_score,e_count],'x':[x_score,x_count]}
        scores_list = sorted(scores.items(), key=lambda s: (s[1][0],-s[1][1]), reverse=True)# 优先分数高，相等时放空位最多的行
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


def nextStep_random(ownBoard,otherBoard,figure):
    # 纯随机，测试用
    index = random.randint(0,8)
    while ownBoard[index] != 0:
        index = random.randint(0,8)
    return index


def nextStep1(ownBoard,otherBoard,figure):
    # 一号机
    # 初始化，用于记录数值
    k_score = 0 # 放置在k行取得的净胜分
    e_score = 0 # 放置在e行取得的净胜分
    x_score = 0 # 放置在x行取得的净胜分
    k_count = 0 # 放置在k行的骰子数
    e_count = 0 # 放置在e行的骰子数
    x_count = 0 # 放置在x行的骰子数
    index = -1

    # 处理K线
    k_score,k_count = calculate_row(ownBoard, otherBoard, 0, 3, figure)
    e_score,e_count = calculate_row(ownBoard, otherBoard, 3, 6, figure)
    x_score,x_count = calculate_row(ownBoard, otherBoard, 6, 9, figure)
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

def nextStep2(ownBoard,otherBoard,figure):
    # 二号机，目前最优
    # 初始化，用于记录数值
    k_score = 0 # 放置在k行取得的净胜分
    e_score = 0 # 放置在e行取得的净胜分
    x_score = 0 # 放置在x行取得的净胜分
    k_count = 0 # 放置在k行的骰子数
    e_count = 0 # 放置在e行的骰子数
    x_count = 0 # 放置在x行的骰子数
    index = -1

    # 处理K线
    k_score,k_count = calculate_row(ownBoard, otherBoard, 0, 3, figure)
    e_score,e_count = calculate_row(ownBoard, otherBoard, 3, 6, figure)
    x_score,x_count = calculate_row(ownBoard, otherBoard, 6, 9, figure)
    # print('k_score = ', k_score,',e_score = ', e_score,',x_score = ',x_score)

    # 建立dict，按照value值对净胜分进行排序，由高到低进行选择
    scores = {'k':[k_score,k_count],'e':[e_score,e_count],'x':[x_score,x_count]}
    scores_list = sorted(scores.items(), key=lambda s: (s[1][0],-s[1][1]), reverse=True)
    # print(scores_list)

    for score in scores_list:
        if score[0][0] == 'k':
            index = place_dice(ownBoard, 0, 3)
        elif score[0][0] == 'e':
            index = place_dice(ownBoard, 3, 6)
        elif score[0][0] == 'x':
            index = place_dice(ownBoard, 6, 9)
        # 找到最优位置，中止循环
        if index != -1:
            break

    return index