from util import _rpc_call
#https://github.com/ethereum/wiki/wiki/JSON-RPC

class Eth(object):

    def protocolVersion(self):
        return _rpc_call("eth_protocolVersion", [])

    @property
    def syncing(self):
        return _rpc_call("eth_syncing", [])
    
    @property
    def coinbase(self):
        return _rpc_call("eth_coinbase", [])

    @property
    def mining(self):
        return _rpc_call("eth_mining", [])
    
    @property
    def hashrate(self):
        return _rpc_call("eth_hashrate", [])

    @property
    def gasPrice(self):
        return _rpc_call("eth_gasPrice", [])

    @property
    def accounts(self):
        return _rpc_call("eth_accounts", [])
    
    @property
    def blockNumber(self):
        return _rpc_call("eth_blockNumber", [])

    def getBalance(self, address, block='latest'):
        return _rpc_call("eth_getBalance", [address, block])

    def getStorageAt(self, address, position, block='latest'):
        return _rpc_call("eth_getStorageAt", [address, position, block])

    #Returns the number of transactions sent from an address.
    def getTransactionCount(self, address, block='latest'):
        if isinstance(block, int):
            block = hex(block)
        return _rpc_call("eth_getTransactionCount", [address, block])

    def getBlockTransactionCountByHash(self, hash):
        return _rpc_call("eth_getBlockTransactionCountByHash", [hash])

    def getBlockTransactionCountByNumber(self, block='latest'):
        if isinstance(block, int):
            block = hex(block)
        num = _rpc_call("eth_getBlockTransactionCountByNumber", [block])
        return int(num,16)
        
    def getUncleCountByBlockHash(self, hash):
        return _rpc_call("eth_getUncleCountByBlockHash", [hash])

    def getUncleCountByBlockNumber(self, block='latest'):
        if isinstance(block, int):
            block = hex(block)
        return _rpc_call("eth_getUncleCountByBlockNumber", [block])

    def getCode(self, block='latest'):
        if isinstance(block, int):
            block = hex(block)
        return _rpc_call("eth_getCode", [block])

    def sign(self, address, data):
        return _rpc_call("eth_sign", [address, data])

    def sendTransaction(self, from_, to_, gas, gasPrice, value, data):
        '''
        params: [{
          "from": "0xb60e8dd61c5d32be8058bb8eb970870f07233155",
          "to": "0xd46e8dd67c5d32be8058bb8eb970870f07244567",
          "gas": "0x76c0", // 30400
          "gasPrice": "0x9184e72a000", // 10000000000000
          "value": "0x9184e72a", // 2441406250
          "data": "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675"
        }]
        '''
        params = [{
          "from": from_,
          "to": to_,
          "gas": hex(gas),
          "gasPrice": hex(gasPrice),
          "value": hex(int(value*1e18)),
          "data": data
        }]

        return _rpc_call("eth_sendTransaction", params)

    def sendRawTransaction(self, data):
        return _rpc_call("eth_sendRawTransaction", [data])

    def call(self, from_, to_, gas, gasPrice, value, data, block='latest'):
        params = [{
          "from": from_,
          "to": to_,
          "gas": hex(gas),
          "gasPrice": hex(gasPrice),
          "value": hex(int(value*1e18)),
          "data": data
        }, block]

        return _rpc_call("eth_call", params)

    def estimateGas(self, from_, to_, gas, gasPrice, value, data):
        params = [{
          "from": from_,
          "to": to_,
          "gas": hex(gas),
          "gasPrice": hex(gasPrice),
          "value": hex(int(value*1e18)),
          "data": data
        }]

        return _rpc_call("eth_estimateGas", params)

    def getBlockByHash(self, hash, full=True):
        return _rpc_call("eth_getBlockByHash", [hash, full])

    def getBlockByNumber(self, block='latest', full=True):
        if isinstance(block, int):
            block = hex(block)
        return _rpc_call("eth_getBlockByNumber", [block, full])

    def getTransactionByHash(self, hash):
        return _rpc_call("eth_getTransactionByHash", [hash])
    
    def getTransactionByBlockHashAndIndex(self, block_hash, ts_index):
        if isinstance(ts_index, int):
            ts_index = hex(ts_index)

        return _rpc_call("eth_getTransactionByBlockHashAndIndex", [block_hash, ts_index])


    def getTransactionByBlockNumberAndIndex(self, block='latest', ts_index=0):
        if isinstance(block, int):
            block = hex(block)
            
        if isinstance(ts_index, int):
            ts_index = hex(ts_index)

        return _rpc_call("eth_getTransactionByBlockNumberAndIndex", [block, ts_index])

    def getTransactionReceipt(self, hash):
        return _rpc_call("eth_getTransactionReceipt", [hash])

    def getUncleByBlockHashAndIndex(self, block_hash, ts_index):
        if isinstance(ts_index, int):
            ts_index = hex(ts_index)

        return _rpc_call("eth_getUncleByBlockHashAndIndex", [block_hash, ts_index])

    def getUncleByBlockNumberAndIndex(self, block='latest', ts_index=0):
        if isinstance(block, int):
            block = hex(block)
            
        if isinstance(ts_index, int):
            ts_index = hex(ts_index)

        return _rpc_call("eth_getUncleByBlockNumberAndIndex", [block, ts_index])


    def getCompilers(self):
        return _rpc_call("eth_getCompilers", [])

    def sign(self, address, data):
        return _rpc_call("eth_sign", [address, data])


    

eth = Eth()


def test():
    currentBlock = eth.syncing.currentBlock
    for i in range(currentBlock):
        n = eth.getBlockTransactionCountByNumber(i)
        if n > 0:
            print(i,n)

