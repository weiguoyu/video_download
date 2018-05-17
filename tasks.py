# -*- coding: utf-8 -*-

import os
import sys
import time
import subprocess
import logging
import logging.handlers
import requests
from celery import (
    Celery,
    platforms
)
from settings import DOWNLOAD_PATH


fm = logging.Formatter('%(asctime)s %(levelname)s %(name)s.%(funcName)s@%(lineno)d %(message)s')
fh = logging.StreamHandler(sys.stdout)
fh.setFormatter(fm)
logger = logging.getLogger(__name__)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


# from celery.utils.log import get_task_logger
#
# logger = get_task_logger(__name__)

# celery 初始化
platforms.C_FORCE_ROOT = True
celery_app = Celery()
celery_app.config_from_object("settings")


# room_ids 初始化
room_ids = []
room_ids_path = os.path.abspath(os.path.dirname(__file__)) + "/room_ids.txt"
with open(room_ids_path) as f:
    for eachline in f:
        if eachline.strip():
            room_ids.append(eachline.strip())
logger.info("room_ids: %s", room_ids)


@celery_app.task(name="test")
def add(x, y):
    return x + y


@celery_app.task(name="video_download", bind=True, max_retries=3)
def video_download(self, url):
    try:
        file_name = url.split("/")[-1]
        date = file_name.split("--")[-1][0:8]
        download_path = os.path.join(DOWNLOAD_PATH, date)
        try:
            if not os.path.exists(download_path):
                os.makedirs(download_path)
        except Exception as exc:
            logger.exception("mkdir failed : %s", exc)
        cmd_str = "wget -c -t 3 %s" % url
        subp = subprocess.Popen(cmd_str, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=download_path, shell=True)
        stdout, stderr = subp.communicate()
        stderr = stderr[0:100]
        returncode = subp.returncode
        if returncode != 0:
            raise Exception(stderr)
        logger.info("video download finished,  url: %s", url)
    except Exception as exc:
        logger.exception("download url %s failed, exception: %s", url, exc)
        raise self.retry(exc=exc, countdown=60)


@celery_app.task(name="get_tasks")
def get_tasks(): 
    current_time = int(time.time())
    start_time = current_time / 3600 * 3600 - 3600 * 6
    end_time = start_time + 3600
    params = {
        "rids": room_ids,
        "starttime": start_time,
        "endtime": end_time
    }
    res = requests.post("http://localhost:5000/api/get_videos", json=params).json()
    logger.debug("res: %s", res)
    records = res.get("result", [])
    records = sorted(records, key=lambda x: x["starttime"])
    for record in records:
       url = record.get("url", None)
       if url:
           video_download.delay(url)
    logger.info("task get_tasks over")

