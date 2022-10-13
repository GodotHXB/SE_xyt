from flask import Flask, render_template, request
import random
from ai import nextStep
import json
import re

app = Flask(__name__)

# url = "http://127.0.0.1/"
# header = {
#     "aaaa": 'token'
# }
# data = {
#     "aaa": True,
#     "bbb": False
# }
# res = requests.post(url=url, headers=header, json=data)
#
# # print(res.content, res.status_code)
# print(res.text, res.status_code)

def random_num():
    return random.randint(1,50)

@app.route('/<board>')
def index(board):
    ownBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    otherBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    figure = 0

    boards = re.findall("\[.*?\]", board)

    index = 0
    nums = re.findall('[0-6]',boards[0])
    for index in range(0,9):
        ownBoard[index] = int(nums[index])

    index = 0
    nums = re.findall('[0-6]',boards[1])
    for index in range(0,9):
        otherBoard[index] = int(nums[index])

    num = re.findall('[0-6]', boards[2])
    figure = int(num[0])

    index = nextStep(ownBoard,otherBoard,figure)
    return str(index)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999, debug=True)