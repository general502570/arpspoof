import mitmproxy
from mitmproxy import *

class MITM:
    def response(self, flow: mitmproxy.http.HTTPFlow):
        f = open("", "r")
        mitm_content = f.read()
        flow.response.set_content(f)

addons = [
    MITM()        
]
