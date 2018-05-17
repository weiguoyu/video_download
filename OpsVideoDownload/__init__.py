# -*- coding: utf-8 -*-

"""
    opOss Blueprint
"""
import sys
import logging
import logging.handlers
from flask import Blueprint

OpsVideoDownloadBP = Blueprint('opsVideoDownload', __name__, url_prefix="/api")

fm = logging.Formatter('%(asctime)s %(levelname)s %(name)s.%(funcName)s@%(lineno)d %(message)s')
fh = logging.StreamHandler(sys.stdout)
fh.setFormatter(fm)
logger = logging.getLogger(__name__)
logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


from .views import *
