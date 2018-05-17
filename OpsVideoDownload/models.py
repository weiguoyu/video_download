# -*- coding: utf-8 -*-


from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String
)
from common.extension import (
    Base,
    db_session
)


class OpsVideoDownload(Base):
    __tablename__ = 'video_rtmp_to_video'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False, default='')
    rid = Column(Integer, nullable=False)
    fsize = Column(BigInteger, nullable=False)
    starttime = Column(Integer, nullable=False)
    endtime = Column(Integer, nullable=False)

    @classmethod
    def get(cls, rids=None, starttime=None, endtime=None):
        session = db_session()
        query = session.query(cls)
        if rids:
            query = query.filter(cls.rid.in_(rids))
        if starttime:
            query = query.filter(cls.starttime >= starttime)
        if endtime:
            query = query.filter(cls.starttime < endtime)
        return query.all()
