from __init__ import db
from models import Users

import json
import os

defaultVal = 100
defaultJson = {}
defaultJson['money'] = 0
defaultJson['numbers'] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
defaultJson['colors'] = [0, 0]


def getQtt(ip):
    user = Users.query.filter_by(ip_address=ip).first()
    if not user:
        new_user = Users(ip_address=ip, val=defaultVal)
        db.session.add(new_user)
        db.session.commit()
        return defaultVal
    else:
        return user.val


def recieveData(ip, data):
    print(data['money'])
    user = Users.query.filter_by(ip_address=ip).first()
    if user:
        qt = int(data['money'])
        for i in data['numbers']:
            qt += int(i)
        for i in data['colors']:
            qt += int(i)

        if qt == int(user.val):
            f = open("data/" + ip + ".json", 'w')
            json.dump(data, f)
            return True
    return False


def validate(ip, val):
    col = 0
    if val == 0:
        pass
    elif val % 2 == 0:
        col = 0 # red = 0
    elif val % 2 == 1:
        col = 1 # black = 1
    if os.path.exists("./data/" + ip + ".json"):
        with open('./data/' + ip + '.json') as file:
            data = json.load(file)
            return int(data['money']) + int(data['numbers'][val]) * 36 + int(data['colors'][col]) * 2

def validateAllUsers(val):
    for user in Users.query:
        user.val = validate(user.ip_address, val)
        db.session.commit()
    folder = './data/'
    for filename in os.listdir(folder):
        os.remove(folder + filename)