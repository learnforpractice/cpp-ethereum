import json
import signal
import atexit

import util
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map

cdef extern from "../eth_.h":
    cdef void handle_request(string& request, string& response)
    cdef void quit_eth()
    cdef string& get_key_()

def rpc_call(request):
    cdef string response
    cdef string request_
    request_ = request
    handle_request(request_, response)
    return util.JsonStruct(response)

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


