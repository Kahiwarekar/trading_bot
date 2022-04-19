import json

f = open("portfolio.json")
p = json.load(f)
print(type(p))
status = p["status"]
data = p["data"]
net = data["net"]
day = data["day"]
netOrderCount = len(net)
dayOrderCount = len(day)

old_PNL = 1500
total_PNL = [0, 0, 0]
for i in range(0, netOrderCount):
    total_PNL.append(net[i]["pnl"])
    newPNL = sum(total_PNL)
print(newPNL)


if newPNL < old_PNL*0.75:
    print("Old PNL was {1} and New PNL is {0}, Action required" .format(newPNL, old_PNL))


