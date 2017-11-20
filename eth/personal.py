from util import _rpc_call

class Personal(object):
    pass



def listAccounts():
    return _rpc_call("personal_listAccounts", [])

def newAccount(passwd):
    return _rpc_call("personal_newAccount", [passwd])

def sendTransaction(from_, to_, value, data, passwd, gas = 0, gasPrice = 0):
    ts = {
      "from": from_,
      "to": to_,
      "value": hex(int(value*1e18)),
      "data": data
    }
    if gas:
        ts['gas'] = hex(gas)
    if gasPrice:
        ts['gasPrice'] = hex(gasPrice)

    params = [ts,passwd]

    return _rpc_call("personal_sendTransaction", params)


def unlockAccount(address, passwd, duration = 300):
    return _rpc_call("personal_unlockAccount", [address, passwd, duration])

personal = Personal()


