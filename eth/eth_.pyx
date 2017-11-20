import json
import util
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp.map cimport map

cdef extern from "../eth_.h":
    cdef extern void handle_request(string& request, string& response)
    cdef extern void quit_eth()

def rpc_call(request):
    cdef string response
    cdef string request_
    request_ = request
    handle_request(request_, response)
    return util.JsonStruct(response)

def signal_handler(signal, frame):
    quit_eth()
    import sys
    sys.exit(0);

def register_signal_handler():
    import signal
    signal.signal(signal.SIGINT, signal_handler)

register_signal_handler()



