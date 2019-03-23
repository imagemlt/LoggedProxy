# -*- coding: utf-8 -*-
import random
import hashlib
import urlparse
from lib.utils import *

def gen_fingerprint(request,poc):
    '''

    :param request:
    :return:
    '''
    # TODO:指纹生成算法
    headers,cookies=parseHeaders(request['headers'])
    url,get_params=url2params(request)
    method=request['method']
    hash_data=poc+method+url
    for k in get_params:
        if k in ['action','method']:
            hash_data=hash_data+' ['+k+','+get_params[k]+']'
        else:
            hash_data=hash_data+' '+k
    if headers.has_key('Content-Type'):
        hash_data=hash_data+' '+headers['Content-Type']
    if method=="POST":
        hash_data=hash_data+" POSTBODY"
        if headers.has_key('Content-Type') and headers['Content-Type']=='application/x-www-form-urlencoded':
            post_params=urlparse.parse_qsl(request['req_body'])
            for k in post_params:
                hash_data=hash_data+' '+k[0]
    m=hashlib.md5()
    m.update(hash_data)
    print hash_data
    hash=m.hexdigest()
    return hash


if __name__=='__main__':
    request={'headers':{'Content-Type':'application/x-www-form-urlencoded'},'method':'POST','url':'http://mdzz.php/imagemlt.php?a=b&c=d&action=post','req_body':'a=b'}
    print gen_fingerprint(request,'XSS')
