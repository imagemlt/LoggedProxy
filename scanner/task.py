# -*- coding: utf-8 -*-
from celery import Celery
from config import config
from proxy.models import *
from scanner.fingerprint import gen_fingerprint

import redis
import json

task=Celery('task',broker=config['redis_broker'],backend=config['redis_backend'])


@task.task
def scan(request):
    redis_conn=redis.StrictRedis(host=config['redis_storage']['host'],port=config['redis_storage']['port'],db=config['redis_storage']['db'])
    fp=gen_fingerprint(request)
    result=redis_conn.sadd('fingerprints',fp)
    scan_res={'request':request}
    if result==0:
        while(redis_conn.llen>=10):
            continue
        scan_res['ans']={'exists':True}
        return scan_res
    '''
    TODO:scan job
    '''
    scan_res['ans'] = {'exists': False}
    scan_res['type']='XSS'
    scan_res['result']='xss in main page'
    return scan_res



