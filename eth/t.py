from admin import miner
from eth import eth
import time

def startMine():
    miner.setEtherbase('0x4b8823fda79d1898bd820a4765a94535d90babf3')
    num = eth.blockNumber
    miner.start()
    while num == eth.blockNumber:
        time.sleep(0.05)
    miner.stop()
    print(eth.blockNumber)
    print('done.')
    