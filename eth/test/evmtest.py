import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider, EthereumTesterProvider
from solc import compile_source
from web3.contract import ConciseContract

class Producer(object):
    def __init__(self, provider):
        self.provider = provider
    
    def produce_block(self):
        self.provider.make_request('test_mineBlocks', [1])

    def __call__(self):
        self.produce_block()

    def __enter__(self):
        pass
    
    def __exit__(self, type, value, traceback):
        self.produce_block()

contract_source_code = '''
pragma solidity ^0.4.0;
contract Greeter {
    mapping(address => uint) public voters;

    function Greeter() {
        sha256('abc');
        keccak256('abc');
        voters[msg.sender] = 128;
    }

    function getHash(uint blockNumber) public returns (bytes32) {
        block.difficulty;
        sha256('+++++++++++++++++++hello, smart contract abcdef');
        voters[msg.sender] = blockNumber;
        return block.blockhash(blockNumber);
    }
    
    function getDiff() public returns (uint) {
        return block.difficulty;
    }
    
}

'''

TEST = False
DEPLOY = True

contract_interface = None
w3 = None
producer = None
contract = None
contract_address = None

provider = HTTPProvider('http://localhost:8545')
producer = Producer(provider)

if TEST:
    w3 = Web3(EthereumTesterProvider())
else:
    w3 = Web3(provider)


def compile():
    global contract_interface
    global producer
    global w3
    global contract
    
    compiled_sol = compile_source(contract_source_code) # Compiled source code
    s = json.dumps(compiled_sol["<stdin>:Greeter"], sort_keys=False, indent=4, separators=(',', ': '))
#    print(s)
    
    contract_interface = compiled_sol['<stdin>:Greeter']
    #print(contract_interface)
    
    # web3.py instance
    #w3 = Web3(TestRPCProvider())
    #w3 = Web3(HTTPProvider())
    
    
    
    # Instantiate and deploy contract
    contract = w3.eth.contract(contract_interface['abi'], bytecode=contract_interface['bin'])
    #print(contract_interface['abi'])
    print(contract_interface['bin'])
    
    json.dumps(contract_interface['abi'], sort_keys=False, indent=4, separators=(',', ': '))

    address = w3.eth.accounts[0]
    print('+++++++++w3.eth.accounts[0]:', address)
    print('+++++++++w3.eth.blockNumber:', w3.eth.blockNumber)

def deploy():
    global contract_address
    with producer:
        # Get transaction hash from deployed contract
        address = w3.eth.accounts[0]
        print('----------w3.eth.blockNumber:', w3.eth.blockNumber)
        with producer:
            tx_hash = contract.deploy(transaction={'from': address, 'gas': 2000001350})
#            tx_hash = contract.deploy(transaction={'from': address})
            print('tx_hash:', tx_hash)
        print('----------w3.eth.blockNumber:', w3.eth.blockNumber)

        # Get tx receipt to get contract address
        tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
##        print('tx_receipt:', tx_receipt)
        contract_address = tx_receipt['contractAddress']
        
        print('-------------------------:', tx_receipt.contractAddress)

##        print(tx_receipt)
        print('contract_address:', contract_address)

#    contract_address = '0x5c5ad149D975c0f6EcB9F19BA2F917AFdCD0AA41'

#0x24bC35FA6f3f81EFD2c7F3ba9862470B805982D3
#0x2445185DDc617d3240d4F0FdA365466CF3CF39F6

contract_instance = None
#personal.unlockAccount(eth.accounts[0],'abc')
'''
args = '0x6b2fafa9000000000000000000000000000000000000000000000000000000000001d0d8'
code = '6060604052341561000f57600080fd5b600260006040516020015260405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060206040518083038160008661646e5a03f1151561006557600080fd5b5050604051805190505060405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060405180910390505060806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550610231806100f96000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630b1bcee71461005c5780636b2fafa914610085578063a3ec138d146100c4575b600080fd5b341561006757600080fd5b61006f610111565b6040518082815260200191505060405180910390f35b341561009057600080fd5b6100a66004808035906020019091905050610119565b60405180826000191660001916815260200191505060405180910390f35b34156100cf57600080fd5b6100fb600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506101ed565b6040518082815260200191505060405180910390f35b600044905090565b6000600260006040516020015260405180807f2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b68656c6c6f2c20736d6172742081526020017f636f6e7472616374206162636465660000000000000000000000000000000000815250602f01905060206040518083038160008661646e5a03f1151561019757600080fd5b50506040518051905050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555081409050919050565b600060205280600052604060002060009150905054815600a165627a7a72305820a170f59df0c8bfb1ce2d223eaabe4cdbb54a4102cf2678d40692e3b03ac8f73f0029'
debug.evm_test(code, args) 

args = '0x6b2fafa9000000000000000000000000000000000000000000000000000000000001d0d8'
code = '6060604052341561000f57600080fd5b600260006040516020015260405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060206040518083038160008661646e5a03f1151561006557600080fd5b5050604051805190505060405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060405180910390505060806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550610231806100f96000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630b1bcee71461005c5780636b2fafa914610085578063a3ec138d146100c4575b600080fd5b341561006757600080fd5b61006f610111565b6040518082815260200191505060405180910390f35b341561009057600080fd5b6100a66004808035906020019091905050610119565b60405180826000191660001916815260200191505060405180910390f35b34156100cf57600080fd5b6100fb600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506101ed565b6040518082815260200191505060405180910390f35b600044905090565b6000600260006040516020015260405180807f2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b68656c6c6f2c20736d6172742081526020017f636f6e7472616374206162636465660000000000000000000000000000000000815250602f01905060206040518083038160008661646e5a03f1151561019757600080fd5b50506040518051905050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555081409050919050565b600060205280600052604060002060009150905054815600a165627a7a72305820a170f59df0c8bfb1ce2d223eaabe4cdbb54a4102cf2678d40692e3b03ac8f73f0029'
debug.evm_test('', code) 

'''

def set_greeting():
    global contract_instance
    print('contract_address:', contract_address)
    address = w3.eth.accounts[0]

    # Contract instance in concise mode
    contract_instance = w3.eth.contract(contract_interface['abi'], contract_address, ContractFactoryClass=ConciseContract)
#    print(dir(contract_instance))

#    r = contract_instance.getDiff(transact={'from': address})
#    print(r)

    r = contract_instance.getHash(119000, transact={'from': address})
    print(r)
    
    if 0:
        with producer:
            contract_instance.setGreeting('Nihao', transact={'from': address})
    
        if 0:
            # Getters + Setters for web3.eth.contract object
            print('Contract value: {}'.format(contract_instance.greet()))
            print('+++++++++w3.eth.blockNumber:', w3.eth.blockNumber)
        
            with producer:
                contract_instance.setGreeting('Nihao', transact={'from': address})
            print('Setting value to: Nihao')
            print('Contract value: {}'.format(contract_instance.greet()))
        
            print('Contract value: {}'.format(contract_instance.helloword()))
            print('Contract getint: {}'.format(contract_instance.getint()))
        
        r = contract_instance.getHash(10).encode('utf8')
        print(len(r))
        
        print('Contract getHash: {}'.format(r))
        
        if 0:
            print('Contract value: {}'.format(contract_instance.getAddress()))

compile()
deploy()
set_greeting()




