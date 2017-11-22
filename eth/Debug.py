from util import _rpc_call

class Debug(object):
    
    def traceTransaction(txHash, json):
        return _rpc_call("debug_traceTransaction", [txHash, json])
    
    def traceBlock(blockRLP, json):
        return _rpc_call("debug_traceBlock", [blockRLP, json])
    
    def traceBlockByHash(blockHash, json):
        return _rpc_call("debug_traceBlockByHash", [blockHash, json])
    
    def traceBlockByNumber(blockNumber, json):
        return _rpc_call("debug_traceBlockByNumber", [blockNumber, json])
    
    def storageRangeAt(blockHashOrNumber, txIndex, address, begin, maxResults):
        return _rpc_call("debug_storageRangeAt", [blockHashOrNumber, txIndex, address, begin, maxResults])
    
    def preimage(hashedKey):
        return _rpc_call("debug_preimage", [hashedKey])

    def traceCall(call, blockNumber, options):
        return _rpc_call("debug_preimage", [call, blockNumber, options])

