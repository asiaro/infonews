#导入 flask 相关模块
from flask import current_app #应用上下文处理 ，处理资源文件
from flask import render_template # 模版处理
from flask import session #coock/session处理
from flask import request #请求上下文处理，处理事件
from flask import jsonify # 处理返回数据使转为json
from flask import abort # 处理异常并提交给服务器

#导入蓝图
from info.home import home_blu #导入蓝图

#导入项目配置处理
from info.utils.response_code import RET, error_map #导入错误码
from info.utils.models import User ,News ,Category#导入数据库相关配置类



@home_blu.route('/favicon.ico')
def favicon():
    response = current_app.send_static_file("new/favicon.ico")

    return response



@home_blu.route('/')
def index():
    pass







