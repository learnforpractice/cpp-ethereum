import eth_
from util import _rpc_call

def eth_setMining(mining, key):
    return _rpc_call("admin_eth_setMining", [mining, key])

def eth_blockQueueStatus(key):
    return _rpc_call("admin_eth_blockQueueStatus", [key])
    
def eth_setAskPrice(price, key):
    if isinstance(price, int):
        price = hex(price)
    return _rpc_call("admin_eth_setAskPrice", [price, key])

def eth_setBidPrice(price, key):
    if isinstance(price, int):
        price = hex(price)
    return _rpc_call("admin_eth_setBidPrice", [price, key])

def eth_findBlock(block_hash, key):
    return _rpc_call("admin_eth_findBlock", [block_hash, key])

def listening():
    return _rpc_call("admin_eth_setBidPrice", [])
    
def peerCount():
    return _rpc_call("net_peerCount", [])

def listening():
    return _rpc_call("net_listening", [])
    
def peerCount():
    return _rpc_call("net_peerCount", [])

def listening():
    return _rpc_call("net_listening", [])
    
def peerCount():
    return _rpc_call("net_peerCount", [])


