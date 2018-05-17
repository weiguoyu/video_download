# -*- coding: utf-8 -*-

"""
    项目功能注册
"""

from .utils import error_resp
from .exc import OpsException

def register_errorhandlers(app):
    """
    注册错误处理.
    Args:
        app: 一个Flask应用实例 或者是蓝图.
    """

    @app.errorhandler(401)
    def unauthorized(error):
        msg = u"对不起, 您没有登录本系统!"
        resp = error_resp(401, msg, 401)
        return resp

    @app.errorhandler(403)
    def forbidden(error):
        msg = u"对不起, 你没有访问该系统的权限! "
        resp = error_resp(403, msg, 403)
        return resp

    @app.errorhandler(404)
    def not_found(error):
        msg = u"找不到你所需的内容! "
        resp = error_resp(404, msg, 404)
        return resp

    @app.errorhandler(405)
    def not_found(error):
        msg = u"对不起,方法错误! "
        resp = error_resp(405, msg, 405)
        return resp

    @app.errorhandler(500)
    def internal(error):
        msg = u"远程服务器返回错误, 请稍后重试! "
        resp = error_resp(500, msg, 500)
        return resp

    @app.errorhandler(OpsException)
    def handle_dns_exception(error):
        resp = error_resp(error.err_code, error.err_msg)
        return resp

    @app.errorhandler(Exception)
    def handle_common_exception(error):
        resp = error_resp(500, getattr(error, "message", "unknown error"), 500)
        return resp
