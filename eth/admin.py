import eth_
from util import _rpc_call

session_key = eth_.get_key()

def setKey(key):
    global session_key
    session_key = key

class Eth(object):
    global session_key
    def setMining(self, mining):
        return _rpc_call("admin_eth_setMining", [mining, session_key])
    
    def blockQueueStatus(self):
        return _rpc_call("admin_eth_blockQueueStatus", [session_key])
        
    def setAskPrice(self, price):
        if isinstance(price, int):
            price = hex(price)
        return _rpc_call("admin_eth_setAskPrice", [price, session_key])
    
    def setBidPrice(self, price):
        if isinstance(price, int):
            price = hex(price)
        return _rpc_call("admin_eth_setBidPrice", [price, session_key])

    def findBlock(self, block_hash):
        return _rpc_call("admin_eth_findBlock", [block_hash, session_key])

    def allAccounts(self):
        return _rpc_call("admin_eth_allAccounts", [session_key])

class Net(object):

    def start(self):
        return _rpc_call("admin_net_start", [session_key])

    def stop(self):
        return _rpc_call("admin_net_stop", [session_key])

    def connect(self, node):
        return _rpc_call("admin_net_connect", [node, session_key])

    @property
    def peers(self):
        key = session_key
        return _rpc_call("admin_net_peers", [session_key])

    @property
    def nodeInfo(self):
        key = session_key
        return _rpc_call("admin_net_nodeInfo", [session_key])

    @property
    def admin_nodeInfo(self):
        return _rpc_call("admin_nodeInfo", [])

    @property
    def admin_peers(self):
        return _rpc_call("admin_peers", [])

    def addPeer(self, node):
        return _rpc_call("admin_addPeer", [node])

class Miner(object):
    
    def start(self):
        return _rpc_call("miner_start", [1])

    def stop(self):
        return _rpc_call("miner_stop", [])

    def setEtherbase(self, uuidOrAddress):
        return _rpc_call("miner_setEtherbase", [uuidOrAddress])

    def setExtra(self, extraData):
        return _rpc_call("miner_setExtra", [extraData])

    def setGasPrice(self, gasPrice):
        gasPrice = hex(gasPrice)
        return _rpc_call("miner_setGasPrice", [gasPrice])

    @property
    def hashrate(self):
        return _rpc_call("miner_hashrate", [])

    def chainInfo(self):
        return _rpc_call("miner_chainInfo", [])



miner = Miner()
eth = Eth()
net = Net()


