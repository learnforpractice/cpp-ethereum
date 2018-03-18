import eth_
from util import _rpc_call

def version():
    return _rpc_call("net_version", [])

def listening():
    return _rpc_call("net_listening", [])
    
def peerCount():
    return _rpc_call("net_peerCount", [])

