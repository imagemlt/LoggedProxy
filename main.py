# -*- coding: utf-8 -*-
from proxy import LoggedProxy


def main():
    LoggedProxy.test(HandlerClass=LoggedProxy.LogRequestHandler)

if __name__=='__main__':
    main()