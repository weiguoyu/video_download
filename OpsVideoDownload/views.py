# -*- coding: utf-8 -*-

import logging
import json
from . import OpsVideoDownloadBP
from common.utils import to_resp
from common.exc import (raise_ops_exc, OpsErrorCode)
from handlers import ops_video_download_hander
from flask import request
# from tasks import (
#     add,
#     video_download
# )

logger = logging.getLogger(__name__)

@OpsVideoDownloadBP.route("/ping", methods=["GET"])
def ping():
    return to_resp(True)


@OpsVideoDownloadBP.route("/get_videos", methods=["POST"])
def get_videos():
    params = json.loads(request.data)
    res = ops_video_download_hander.get(**params)
    return to_resp(res)


# @OpsVideoDownloadBP.route("/test", methods=["GET"])
# def test():
#     add.delay(1, 1)
#     return to_resp(True)
#
#
# @OpsVideoDownloadBP.route("/download", methods=["POST"])
# def download():
#     params = json.loads(request.data)
#     url = params.get("url", None)
#     if not url:
#         raise_ops_exc(OpsErrorCode.PARAMETER_ERROR, u"url 不能为空")
#     video_download.delay(url)
#     return to_resp(True)
