# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Text, DateTime, Integer, Boolean, ForeignKey, create_engine
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
    sended=Column(Boolean,default=False)
    dealed=Column(Boolean,default=False)

class Result(Base):
    __tablename__='Result'

    id=Column(Integer,primary_key=True,autoincrement=True)
    requestId=Column(Integer,ForeignKey('Log.id'))
    fingerprint=Column(String(1024))
    type=Column(String(20))
    time = Column(DateTime, default=datetime.datetime.utcnow())
    result=Column(Text)




engine=create_engine('sqlite:////tmp/log.db')

Base.metadata.create_all(engine)

DBSession =sessionmaker(bind=engine)

