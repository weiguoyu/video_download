# -*- coding: utf-8 -*-

import os
import sys
import requests
from tasks import video_download

room_ids = []
room_ids_path = os.path.abspath(os.path.dirname(__file__)) + "/room_ids.txt"
with open(room_ids_path) as f:
    for eachline in f:
        if eachline.strip():
            room_ids.append(eachline.strip())
print "room_ids: %s" % room_ids


if __name__ == '__main__':
    start_time = sys.argv[1]
    end_time = sys.argv[2]
    print "start_time: %s end_time: %s" % (start_time, end_time)
    params = {
        "rids": room_ids,
        "starttime": start_time,
        "endtime": end_time
    }
    res = requests.post("http://localhost:5000/api/get_videos", json=params).json()
    print "res: %s", res
    records = res.get("result", [])
    records = sorted(records, key=lambda x: x["starttime"])
    for record in records:
       url = record.get("url", None)
       if url:
           video_download.delay(url)
    print "supply data over"
