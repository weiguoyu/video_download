# -*- coding: utf-8 -*-

from .models import OpsVideoDownload
from .schema import OpsVideoDownloadSchema


class OpsVideoDownloadHandler(object):
    def get(self, **kwargs):
        rids = kwargs.get("rids", None)
        starttime = kwargs.get("starttime", None)
        endtime = kwargs.get("endtime", None)

        records = OpsVideoDownload.get(rids=rids, starttime=starttime, endtime=endtime)
        record_json_list = OpsVideoDownloadSchema(many=True).dump(records).data
        return record_json_list



ops_video_download_hander = OpsVideoDownloadHandler()
