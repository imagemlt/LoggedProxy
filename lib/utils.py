# -*- coding: utf-8 -*-
import requests
import urlparse
def cookie2jar(cookies):
    cookie=cookies.strip(';').split(';')
    cookie_dict={}
    for cook in cookie:
        k,v=cook.strip().split('=',1)
        cookie_dict[k]=v
    cookiesJar=requests.utils.cookiejar_from_dict(cookie_dict,cookiejar=None,overwrite=True)
    return cookiesJar

def parseHeaders(headers):
    heads={}
    cookiesJar=None
    for head in headers:
        if(head != 'Cookie'):
            heads[head]=headers[head]
        else:
            cookiesJar=cookie2jar(headers[head])
    return heads,cookiesJar

def req2file(request):
    result=request['requestline']
    for head in request['headers']:
        result=result+"\r\n"+head+":"+request['headers'][head]
    result=result+"\r\n\r\n"+request['req_body']
    return result


def url2params(request):
    url=request['url'].split('?',1)
    query = urlparse.urlparse(request['url']).query
    return url[0],dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])

