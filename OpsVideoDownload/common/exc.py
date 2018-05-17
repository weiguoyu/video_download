# -*- coding: utf-8 -*-

"""
    异常
"""

class OpsException(Exception):
    def __init__(self, err_code, err_msg):
        self.err_code = err_code
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg


def raise_ops_exc(err_code, err_msg=None):
    """
        OPS异常
    Args:
        err_code (int): 错误码
        err_msg (string): 错误信息
    """
    err_msg = err_msg or TRANSLATIONS.get(err_code, u"")
    raise OpsException(err_code, err_msg)


class OpsErrorCode(object):
    """
    错误码
    """
    UNKNOWN_ERROR = 0
    DATABASE_ERROR = 1
    SYSTEM_INTERNAL_ERROR = 2
    RECORD_NOT_FOUND = 3
    PARAMETER_ERROR = 4


TRANSLATIONS = {
    OpsErrorCode.UNKNOWN_ERROR: u"系统异常, 请稍后再试",
    OpsErrorCode.DATABASE_ERROR: u"数据库错误",
    OpsErrorCode.SYSTEM_INTERNAL_ERROR: u"系统内部错误",
    OpsErrorCode.RECORD_NOT_FOUND: u"记录不存在",
    OpsErrorCode.PARAMETER_ERROR: u"参数解析错误",
}


