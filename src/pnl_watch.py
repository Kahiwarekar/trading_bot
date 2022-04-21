import read_portfolio
import time
pnl_value = 0
while True:
    old_PNL = pnl_value
    time.sleep(60)
    pnl_value = read_portfolio.net_pnl()
    if pnl_value < old_PNL*0.75:
        print("Old PNL was {1} and New PNL is {0}, Action required" .format(pnl_value, old_PNL))
    break