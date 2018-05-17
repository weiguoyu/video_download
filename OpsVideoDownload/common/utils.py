#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Response


def page_consersion(page_no, page_size):
    """
    将分页参数从page_no page_size转换为offset limit
    Args:
        page_no (int): 页号
        page_size (int): 分页大小

    Returns:
        offset (int): 偏移量
        limit (int): 个数
    """
    limit = page_size
    offset = (page_no - 1) * page_size
    return offset, limit

def to_resp(data, code=200):
    """
    将一条数据处理成Response.

    Args:
        data: 要处理的数据.
        code: 状态码
    Returns:
        Http Response
    """
    message = {
        'code': code,
        'result': data
    }
    return Response(json.dumps(message))

def error_resp(code, msg, resp_code=200):
    """
    生成错误相应．
    Args:
        code (int): 错误码.
        msg (string): 错误信息
    Returns:
        Http Response
    """
    message = {
        'code': code,
        'msg': msg
    }
    resp = Response(json.dumps(message))
    resp.status_code = resp_code
    return resp
