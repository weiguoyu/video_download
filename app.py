# -*- coding: utf-8 -*-

from flask import Flask
from OpsVideoDownload import OpsVideoDownloadBP
from OpsVideoDownload.common.registers import register_errorhandlers
from OpsVideoDownload.common.extension import register_db_session


app = Flask(__name__)
app.config.from_pyfile("settings.py")

# 注册异常处理
register_errorhandlers(app)

# 蓝图注册
app.register_blueprint(OpsVideoDownloadBP)

# 注册db_session 处理函数
register_db_session(app)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)

