import json
import eth_

id = 0
rpc = {"jsonrpc":"2.0","method":"web3_clientVersion","params":[],"id":67}

def _rpc_call(method, params):
    global id
    id = id + 1
    rpc['id'] = id
    rpc['method'] = method
    rpc['params'] = params
#    print(str(rpc))

    request = json.dumps(rpc)
    request = bytes(request,'utf8')

    ret = eth_.rpc_call(request)
#    print(ret)
    if hasattr(ret,'result'):
        return ret.result
    print(request)
    raise Exception(str(ret))


class JsonStruct(object):
    def __init__(self, js):
        if isinstance(js, bytes):
            js = js.decode('utf8')
            js = json.loads(js)
            if isinstance(js, str):
                js = json.loads(js)
        for key in js:
            value = js[key]
            if isinstance(value, dict):
                self.__dict__[key] = JsonStruct(value)
            elif isinstance(value, list):
                for i in range(len(value)):
                    v = value[i]
                    if isinstance(v, dict):
                        value[i] = JsonStruct(v)
                self.__dict__[key] = value
            else:
                self.__dict__[key] = value
    def __str__(self):
        return str(self.__dict__)
#        return json.dumps(self, default=lambda x: x.__dict__,sort_keys=False,indent=4, separators=(',', ': '))
    def __repr__(self):
        return json.dumps(self, default=lambda x: x.__dict__, sort_keys=False, indent=4, separators=(',', ': '))

