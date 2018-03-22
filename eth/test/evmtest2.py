import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider, EthereumTesterProvider
from solc import compile_source
from web3.contract import ConciseContract

class Producer(object):
    def __init__(self, provider):
        self.provider = provider
    
    def produce_block(self):
        pass
#        self.provider.make_request('test_mineBlocks', [1])

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
        voters[msg.sender] = 31415926;
    }

    function getHash(uint blockNumber) public returns (bytes32) {
        block.difficulty;
        sha256('+++++++++++++++++++hello, smart contract abcdef');
        voters[msg.sender] = blockNumber;
        return block.blockhash(blockNumber);
    }

    function getValue() public returns (uint) {
        block.difficulty;
        sha256('+++++++++++++++++++hello, smart contract abcdef');
        return voters[msg.sender];
    }

    function setValue(uint v) public {
        voters[msg.sender] = v;
        v = voters[msg.sender];
    }

    function getDiff() public returns (uint) {
        return block.difficulty;
    }
    
}

'''
        
contract_source_code = '''
pragma solidity ^0.4.0;

/**
 * @title SafeMath
 * @dev Math operations with safety checks that throw on error
 */
library SafeMath {
  function mul(uint256 a, uint256 b) internal pure returns (uint256) {
    uint256 c = a * b;
    assert(a == 0 || c / a == b);
    return c;
  }

  function div(uint256 a, uint256 b) internal pure returns (uint256) {
    // assert(b > 0); // Solidity automatically throws when dividing by 0
    uint256 c = a / b;
    // assert(a == b * c + a % b); // There is no case in which this doesn't hold
    return c;
  }

  function sub(uint256 a, uint256 b) internal pure returns (uint256) {
    assert(b <= a);
    return a - b;
  }

  function add(uint256 a, uint256 b) internal pure returns (uint256) {
    uint256 c = a + b;
    assert(c >= a);
    return c;
  }
}

/**
 * @title ERC20 interface
 * @dev see https://github.com/ethereum/EIPs/issues/20
 */
contract ERC20 {
  uint256 public totalSupply;
  function balanceOf(address who) public view returns (uint256);
  function transfer(address to, uint256 value) public returns (bool);
  function allowance(address owner, address spender) public view returns (uint256);
  function transferFrom(address from, address to, uint256 value) public returns (bool);
  function approve(address spender, uint256 value) public returns (bool);
  event Transfer(address indexed from, address indexed to, uint256 value);
  event Approval(address indexed owner, address indexed spender, uint256 value);
}

/**
 * @title Standard ERC20 token
 *
 * @dev Implementation of the basic standard token.
 * @dev https://github.com/ethereum/EIPs/issues/20
 * @dev Based on code by FirstBlood: https://github.com/Firstbloodio/token/blob/master/smart_contract/FirstBloodToken.sol
 */
contract StandardToken is ERC20 {
  using SafeMath for uint256;

  mapping(address => uint256) balances;
  mapping(address => address) balances2;
  mapping (address => mapping (address => uint256)) allowed;

  /**
   * @dev Gets the balance of the specified address.
   * @param _owner The address to query the the balance of.
   * @return An uint256 representing the amount owned by the passed address.
   */
  function balanceOf(address _owner) public view returns (uint256 balance) {
    return balances[_owner];
  }

  /**
   * @dev transfer token for a specified address
   * @param _to The address to transfer to.
   * @param _value The amount to be transferred.
   */
  function transfer(address _to, uint256 _value) public returns (bool) {
    require(_to != address(0));

    // SafeMath.sub will throw if there is not enough balance.
    balances[msg.sender] = balances[msg.sender].sub(_value);
    balances[_to] = balances[_to].add(_value);
    Transfer(msg.sender, _to, _value);
    return true;
  }

  /**
   * @dev Transfer tokens from one address to another
   * @param _from address The address which you want to send tokens from
   * @param _to address The address which you want to transfer to
   * @param _value uint256 the amount of tokens to be transferred
   */
  function transferFrom(address _from, address _to, uint256 _value) public returns (bool) {
    var _allowance = allowed[_from][msg.sender];
    require(_to != address(0));
    require (_value <= _allowance);
    balances[_from] = balances[_from].sub(_value);
    balances[_to] = balances[_to].add(_value);
    allowed[_from][msg.sender] = _allowance.sub(_value);
    Transfer(_from, _to, _value);
    return true;
  }

  /**
   * @dev Approve the passed address to spend the specified amount of tokens on behalf of msg.sender.
   * @param _spender The address which will spend the funds.
   * @param _value The amount of tokens to be spent.
   */
  function approve(address _spender, uint256 _value) public returns (bool) {
    // To change the approve amount you first have to reduce the addresses`
    //  allowance to zero by calling `approve(_spender, 0)` if it is not
    //  already 0 to mitigate the race condition described here:
    //  https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
    require((_value == 0) || (allowed[msg.sender][_spender] == 0));
    allowed[msg.sender][_spender] = _value;
    Approval(msg.sender, _spender, _value);
    return true;
  }

  /**
   * @dev Function to check the amount of tokens that an owner allowed to a spender.
   * @param _owner address The address which owns the funds.
   * @param _spender address The address which will spend the funds.
   * @return A uint256 specifying the amount of tokens still available for the spender.
   */
  function allowance(address _owner, address _spender) public view returns (uint256 remaining) {
    return allowed[_owner][_spender];
  }
}

contract MotionToken is StandardToken {
  string public constant name = "Motion Token";
  string public constant symbol = "MTN";
  uint8 public constant decimals = 18;
  uint256 public totalSupply2;

  function MotionToken() public {
    totalSupply = 2100000000000000000000000000;
    balances[msg.sender] = totalSupply;
    balances[1] = 12345678;
    balances[2] = balances[1];
  }
}
'''

from eth_utils import (
    to_dict,
)

class LocalProvider(web3.providers.base.JSONBaseProvider):
    endpoint_uri = None
    _request_args = None
    _request_kwargs = None

    def __init__(self, endpoint_uri, request_kwargs=None):
        self.endpoint_uri = endpoint_uri
        self._request_kwargs = request_kwargs or {}
        super(LocalProvider, self).__init__()

    def __str__(self):
        return "RPC connection {0}".format(self.endpoint_uri)

    @to_dict
    def get_request_kwargs(self):
        if 'headers' not in self._request_kwargs:
            yield 'headers', self.get_request_headers()
        for key, value in self._request_kwargs.items():
            yield key, value

    def get_request_headers(self):
        return {
            'Content-Type': 'application/json',
            'User-Agent': construct_user_agent(str(type(self))),
        }

    def make_request(self, method, params):
        print('+++++++++++++', method, params)
        request_data = self.encode_rpc_request(method, params)
        raw_response = make_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        return response

TEST = False
DEPLOY = True

contract_interface = None
w3 = None
producer = None
contract = None
contract_address = None

provider = LocalProvider('http://localhost:8545')
producer = Producer(provider)

if TEST:
    w3 = Web3(EthereumTesterProvider())
else:
    w3 = Web3(provider)

#"<stdin>:Greeter"
def compile(main_class):
    global contract_interface
    global producer
    global w3
    global contract
    
    compiled_sol = compile_source(contract_source_code) # Compiled source code
    
    for key in compiled_sol.keys():
        print(key)
        
    s = json.dumps(compiled_sol[main_class], sort_keys=False, indent=4, separators=(',', ': '))
#    print(s)
    
    contract_interface = compiled_sol[main_class]
    #print(contract_interface)
    
    # web3.py instance
    #w3 = Web3(TestRPCProvider())
    #w3 = Web3(HTTPProvider())
    
    
    
    # Instantiate and deploy contract
    contract = w3.eth.contract(contract_interface['abi'], bytecode=contract_interface['bin'])
    #print(contract_interface['abi'])
    print(contract_interface['bin'])
    with open('/Users/newworld/dev/pyeos/build/programs/mtn.bin', 'w') as f:
        f.write(contract_interface['bin'])

    json.dumps(contract_interface['abi'], sort_keys=False, indent=4, separators=(',', ': '))


def deploy():
    global contract_address
    with producer:
        # Get transaction hash from deployed contract
        address = '0x5c5ad149D975c0f6EcB9F19BA2F917AFdCD0AA41' #w3.eth.accounts[0]
        with producer:
            tx_hash = contract.deploy(transaction={'from': address, 'gas': 2000001350})
#            tx_hash = contract.deploy(transaction={'from': address})
            print('tx_hash:', tx_hash)

#    contract_address = '0x5c5ad149D975c0f6EcB9F19BA2F917AFdCD0AA41'

#0x24bC35FA6f3f81EFD2c7F3ba9862470B805982D3
#0x2445185DDc617d3240d4F0FdA365466CF3CF39F6

contract_instance = None
#personal.unlockAccount(eth.accounts[0],'abc')
'''
args = '0x6b2fafa9000000000000000000000000000000000000000000000000000000000001d0d8'
code = '6060604052341561000f57600080fd5b600260006040516020015260405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060206040518083038160008661646e5a03f1151561006557600080fd5b5050604051805190505060405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060405180910390505060806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550610231806100f96000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630b1bcee71461005c5780636b2fafa914610085578063a3ec138d146100c4575b600080fd5b341561006757600080fd5b61006f610111565b6040518082815260200191505060405180910390f35b341561009057600080fd5b6100a66004808035906020019091905050610119565b60405180826000191660001916815260200191505060405180910390f35b34156100cf57600080fd5b6100fb600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506101ed565b6040518082815260200191505060405180910390f35b600044905090565b6000600260006040516020015260405180807f2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b68656c6c6f2c20736d6172742081526020017f636f6e7472616374206162636465660000000000000000000000000000000000815250602f01905060206040518083038160008661646e5a03f1151561019757600080fd5b50506040518051905050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555081409050919050565b600060205280600052604060002060009150905054815600a165627a7a72305820a170f59df0c8bfb1ce2d223eaabe4cdbb54a4102cf2678d40692e3b03ac8f73f0029'
debug.evm_test(code, args) 

code = '6060604052341561000f57600080fd5b600260006040516020015260405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060206040518083038160008661646e5a03f1151561006557600080fd5b5050604051805190505060405180807f6162630000000000000000000000000000000000000000000000000000000000815250600301905060405180910390505060806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002081905550610231806100f96000396000f300606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630b1bcee71461005c5780636b2fafa914610085578063a3ec138d146100c4575b600080fd5b341561006757600080fd5b61006f610111565b6040518082815260200191505060405180910390f35b341561009057600080fd5b6100a66004808035906020019091905050610119565b60405180826000191660001916815260200191505060405180910390f35b34156100cf57600080fd5b6100fb600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506101ed565b6040518082815260200191505060405180910390f35b600044905090565b6000600260006040516020015260405180807f2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b68656c6c6f2c20736d6172742081526020017f636f6e7472616374206162636465660000000000000000000000000000000000815250602f01905060206040518083038160008661646e5a03f1151561019757600080fd5b50506040518051905050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555081409050919050565b600060205280600052604060002060009150905054815600a165627a7a72305820a170f59df0c8bfb1ce2d223eaabe4cdbb54a4102cf2678d40692e3b03ac8f73f0029'
debug.evm_test('', code) 

args = '0x6b2fafa9000000000000000000000000000000000000000000000000000000000001d0d8'
code = '606060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680630b1bcee71461005c5780636b2fafa914610085578063a3ec138d146100c4575b600080fd5b341561006757600080fd5b61006f610111565b6040518082815260200191505060405180910390f35b341561009057600080fd5b6100a66004808035906020019091905050610119565b60405180826000191660001916815260200191505060405180910390f35b34156100cf57600080fd5b6100fb600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506101ed565b6040518082815260200191505060405180910390f35b600044905090565b6000600260006040516020015260405180807f2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b2b68656c6c6f2c20736d6172742081526020017f636f6e7472616374206162636465660000000000000000000000000000000000815250602f01905060206040518083038160008661646e5a03f1151561019757600080fd5b50506040518051905050816000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000208190555081409050919050565b600060205280600052604060002060009150905054815600a165627a7a72305820a170f59df0c8bfb1ce2d223eaabe4cdbb54a4102cf2678d40692e3b03ac8f73f0029'
debug.evm_test(code, args) 


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

    r = contract_instance.setValue(119000, transact={'from': address})
    print('++++++++++++setValue:', r)

#    r = contract_instance.getValue(transact={'from': address})
#    r = contract_instance.getValue(call={'from': address})
    r = contract_instance.getValue(call={})
    print('++++++++++getValue:', r)

#    r = contract_instance.getHash(119000, transact={'from': address})
#    print(r)
    
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

#name = "<stdin>:Greeter"
name = "<stdin>:MotionToken"
compile(name)

deploy()
set_greeting()




