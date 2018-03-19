import json
import signal
import atexit

from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map

cdef extern from "../eth_.h":
    cdef void handle_request(string& request, string& response)
    cdef void quit_eth()
    cdef string& get_key_()


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

def rpc_call(request):
    cdef string response
    cdef string request_
    request_ = request
    handle_request(request_, response)
    return JsonStruct(response)

def get_key():
    key = get_key_()
    return key.decode('utf8')

def signal_handler(signal, frame):
    quit_eth()
    import sys
    sys.exit(0);

def register_signal_handler():
    signal.signal(signal.SIGINT, signal_handler)

def on_python_exit():
    quit_eth()

register_signal_handler()
atexit.register(on_python_exit)


