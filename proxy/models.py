# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Text, DateTime, Integer ,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Log(Base):
    # 表示请求记录
    __tablename__ = 'Log'

    # 表结构

    id=Column(Integer,primary_key=True,autoincrement=True)
    method=Column(String(20)) # 请求方法
    url=Column(String(1024))
    requestline=Column(String(1024))
    headers=Column(String(1024))
    req_body=Column(Text,nullable=True)
    time=Column(DateTime,default=datetime.datetime.utcnow())



engine=create_engine('sqlite:////tmp/log.db')

Base.metadata.create_all(engine)

DBSession =sessionmaker(bind=engine)

