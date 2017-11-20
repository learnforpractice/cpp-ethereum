import eth_
from util import _rpc_call

class Web3(object):

    def clientVersion():
        return _rpc_call("web3_clientVersion", [])
    
    def sha3(value):
        return _rpc_call("web3_sha3", [value])
    
    def net_version():
        return _rpc_call("net_version", [])
    
    def net_peerCount():
        return _rpc_call("net_peerCount", [])

web = Web3()


    



