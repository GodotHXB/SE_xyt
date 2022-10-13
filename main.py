import settings
import ai
from local_competition import *


def print_welcome_msg():
    print('''
    欢迎来到逍遥骰
   输入数字选择模式：
     1.本地对战
     2.人机对战
     3.在线对战
    ''')


def main():
    print_welcome_msg()
    mode = int(input('请输入想选择的模式：'))
    if mode == 1:
        start_game_local()
    if mode == 2:
        start_game_ai()
    if mode == 3:
        pass


if __name__ == '__main__':
    main()


