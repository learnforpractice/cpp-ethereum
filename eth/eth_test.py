from util import _rpc_call
#https://github.com/ethereum/wiki/wiki/JSON-RPC

class Test(object):

    def setChainParams(self, param1):
        return _rpc_call("test_setChainParams", [param1])

    def mineBlocks(self, number):
        return _rpc_call("test_mineBlocks", [number])

    def modifyTimestamp(self, timestamp):
        return _rpc_call("test_modifyTimestamp", [timestamp])

    def addBlock(self, rlp):
        return _rpc_call("test_addBlock", [rlp])

    def rewindToBlock(self, number):
        return _rpc_call("test_rewindToBlock", [number])

test = Test()



