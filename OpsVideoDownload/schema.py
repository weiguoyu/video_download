# -*- coding: utf-8 -*-

"""
    Schema模块
"""

from marshmallow import Schema, fields

class OpsVideoDownloadSchema(Schema):
    """ OpsVideoDownload类的Schema类
    """
    id = fields.Int()
    url = fields.Str()
    rid = fields.Int()
    fsize = fields.Int()
    starttime = fields.Int()
    endtime = fields.Int()
