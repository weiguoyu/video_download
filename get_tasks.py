# -*- coding: utf-8 -*-

import os
from app import app
from OpsVideoDownload.handlers import ops_video_download_hander

room_ids = []
room_ids_path = os.path.abspath(os.path.dirname(__file__)) + "/room_ids.txt"
with open(room_ids_path) as f:
    for eachline in f:
        if eachline.strip():
            room_ids.append(eachline.strip())
print "room_ids: %s" % room_ids



if __name__ == "__main__":
    with app.app_context():
        records = ops_video_download_hander.get(rids=room_ids, starttime=1526554800, endtime=1526562000)
        print records

