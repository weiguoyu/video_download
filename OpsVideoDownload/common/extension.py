#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    数据库连接配置
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import (
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_ECHO,
    SQLALCHEMY_POOL_RECYCLE
)

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True, echo=SQLALCHEMY_ECHO, pool_recycle=SQLALCHEMY_POOL_RECYCLE)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()


def register_db_session(app):
    """
        注册数据库连接处理信息
        Args:
            app: Flask应用实例.
    """
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
