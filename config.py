# -*- coding: utf-8 -*-
config={
    'redis_broker':'redis://localhost:6379/0',
    'redis_backend':'redis://localhost:6379/0',
    'redis_storage':{
        'host':'127.0.0.1',
        'port':6379,
        'db':1
    },
    'tasks':10,
    'pocs':['xss'],
    'poc_path':'/Users/image/PycharmProjects/PScan/lib/pocs/',
    'poc_config':{
      'xss':{
        'xss_str':'<script>alert(1)</script>'
      }
    },
    'enable_sqlmap':True,
    'sqlmap_api':'http://127.0.0.1:8775',
    'sqlmap':{
      'ban':[]
    },
    'log':{
      "version": 1,
      "disable_existing_loggers": False,

      #  日志格式
      "formatters": {
        "simple": {
          "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
      },

      "handlers": {

        #      定义控制台日志的级别和样式
        "console": {
          "class": "logging.StreamHandler",
          "level": "DEBUG",
          "formatter": "simple",
          "stream": "ext://sys.stdout"
        },

        #        定义INFO（以上）级别的日志处理器
        "info_file_handler": {
          "class": "logging.handlers.RotatingFileHandler",
          "level": "INFO",
          "formatter": "simple",
          "filename": "./logs/info.log",
          "maxBytes": 10485760,
          "backupCount": 20,
          "encoding": "utf8"
        },

        #        定义ERROR以上）级别的日志处理器
        "error_file_handler": {
          "class": "logging.handlers.RotatingFileHandler",
          "level": "ERROR",
          "formatter": "simple",
          "filename": "./logs/errors.log",
          "maxBytes": 10485760,
          "backupCount": 20,
          "encoding": "utf8"
        }
      },

      #    定义不同name的logger的日志配置
      "loggers": {
        "mymodule": {
          "level": "ERROR",
          "handlers": [
            "info_file_handler"
          ],
          "propagate": "no"
        }
      },

      #   定义全局日志配置
      "root": {
        "level": "DEBUG",
        "handlers": [
          "console",
          "info_file_handler",
          "error_file_handler"
        ]
      }
    }


}