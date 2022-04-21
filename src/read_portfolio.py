import json
import constant
import os.path

def __get_data():
    f = open(os.path.dirname(__file__) + '\\..\\data\\portfolio.json')
    p = json.load(f)
    return p

def net_pnl():
    positions = __get_data()

    status = positions[constant.status]
    if status == "success":
        data = positions[constant.data]
        net = data[constant.net]
        netOrderCount = len(net)
        total_PNL = []

        for i in range(0, netOrderCount):
            total_PNL.append(net[i]["pnl"])
            new_pnl = sum(total_PNL)
        return new_pnl





