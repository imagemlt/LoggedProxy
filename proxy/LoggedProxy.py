# -*- coding: utf-8 -*-
from models import *
from proxy2 import *
import json


class LogRequestHandler(ProxyRequestHandler):
    def request_handler(self, req, req_body):
        session=DBSession()
        log=Log()
        log.method=req.command
        log.url=req.path
        log.requestline=req.raw_requestline
        log.headers=json.dumps(dict(req.headers))
        log.req_body=req_body
        session.add(log)
        session.commit()
        session.close()

def test(HandlerClass=ProxyRequestHandler, ServerClass=ThreadingHTTPServer, protocol="HTTP/1.1"):
    if sys.argv[1:]:
        ip=sys.argv[1]
        port = int(sys.argv[2])
    else:
        ip="::1"
        port = 5678
    server_address = (ip, port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print "Serving HTTP Proxy on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()

if __name__ == '__main__':
    test(HandlerClass=LogRequestHandler)
