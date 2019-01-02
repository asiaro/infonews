import logging #导入日志处理模块
from logging.handlers import RotatingFileHandler#日志回滚模块(当日志文件大于某值时新开日志)同有TimedRotatingFileHandler（当到达某时间时新开日志）

from flask import Flask #导入flask
from flask_sqlalchemy import SQLAlchemy#导入数据库处理模块
from redis import Redis#导入redis数据库处理模块
from flask_migrate import Migrate#导入数据迁移模块
from flask_session import Session#flask_session将session的值存储在redis/Memcached中（保护session数据）

from config import config_dict#导入配置类字典用于工厂函数处理


def create_app(config_type):

    config_class=config_dict[config_type]
    app = False(__name__)

    app.config.from_object(config_class)
    global db ,rs #声明全局变量

    db=SQLAlchemy(app)

    rs=Redis(host=config_class.REDIS_HOST,port=config_class.REDIS_PORT)

    Session(app)#初始化session存储对象

    Migrate(app,db)


    #导入蓝图用于对模块外声明
    #为避免导入错误，对于只使用一次的内容，在使用前导入
    #主页面
    from info.modules.home import home_blu
    app.register_blueprint(home_blu)
    #注册页面
    from info.modules.passport import passport_blu
    app.register_blueprint(passport_blu)
    #新闻页面
    from info.modules.news import news_blu
    app.register_blueprint(news_blu)
    #用户界面
    from info.modules.user import user_blu
    app.register_blueprint(user_blu)


    # 项目关联模型文件   import *语法不能在函数/方法中使用
    # from info import models
    import info.utils.models

    setup_log(config_class.LOGLEVEL)
    

    return app



#日志配置函数 (将flask内置的日志和自定义的日志保存到文件中)
def setup_log(log_levenl):
    logging.basicConfig(level=log_levenl)


    file_log_handler=RRotatingFileHandler("logs/log",maxBytes=1024*1024*100,backCount=10)

    formatter=logging.Formatter('%(levelname)s%(pathname)s:%(lineno)d %(message)s')

    file_log_handler.setFormatter(formatter)

    logging.getLogger().addHandler(file_log_handler)


