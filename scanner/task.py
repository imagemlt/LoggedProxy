# -*- coding: utf-8 -*-
from celery import Celery
from config import config
from proxy.models import *
from scanner.fingerprint import gen_fingerprint
from lib.Log import *
import requests
import time
import redis
import json
import os
import imp

task=Celery('task',broker=config['redis_broker'],backend=config['redis_backend'])


@task.task
def scan(request,poc):
    poc=poc.replace('..','')
    redis_conn=redis.StrictRedis(host=config['redis_storage']['host'],port=config['redis_storage']['port'],db=config['redis_storage']['db'])
    fp=gen_fingerprint(request,poc)
    result=redis_conn.sadd('fingerprints',fp)
    scan_res={'request':request,"exists":False,'found':False}
    if result==0:
        scan_res['exists']=True
        return scan_res
    try:
        poc_script=config['poc_path']+"/"+poc+".py"
        if os.path.exists(poc_script):
            module=imp.load_source('POC_'+poc,poc_script)
            exists,description=module.poc(request,config['poc_config'][poc])
            scan_res['found'] = exists
            scan_res['result'] = description
    except Exception,e:
        logging.error(e.message)
    finally:
        scan_res['type']=poc
        return scan_res


@task.task
def sqlmap_scan(request):
    # GourdScan项目中的代码复用过来的
    redis_conn = redis.StrictRedis(host=config['redis_storage']['host'], port=config['redis_storage']['port'],
                                   db=config['redis_storage']['db'])
    fp=gen_fingerprint(request,'SQLMAP')
    message = {'request': request, 'type': 'SQLMAP', 'found': 0, "result": "","exists":False}
    if redis_conn.sadd('fingerprints',fp)==0:
        message['exists']=True
        return message
    sqlmap_api=config['sqlmap_api']
    sqlmap_conf=config['sqlmap']
    conf_ban = ["url", "headers", "data", "taskid", "database"]
    for ban in conf_ban:
        if ban in sqlmap_conf.keys():
            del sqlmap_conf[ban]
    sqlmap_conf['url']=request['url']
    sqlmap_conf['data']=request['req_body']
    sqlmap_conf['headers']=""
    for header in request['headers']:
        sqlmap_conf['headers']+="%s: %s\r\n"%(header,request['headers'][header])

    json_headers={'Content-Type':'application/json'}
    taskid=json.loads(requests.get('%s/task/new'%(sqlmap_api)).content)['taskid']
    data=json.dumps(sqlmap_conf)
    try:
        requests.post("%s/scan/%s/start"%(sqlmap_api,taskid),data=json.dumps(sqlmap_conf),headers=json_headers)

        while(json.loads(requests.get("%s/scan/%s/status"%(sqlmap_api,taskid)).content)['status']!='terminated'):
            time.sleep(5)
        data=json.loads(requests.get("%s/scan/%s/data"%(sqlmap_api,taskid)).content)['data']
        if data!=[]:
            message['found']=3
            message['result'] += json.dumps(data)
    except Exception,e:
        logging.error(e.message)
    finally:
        return message