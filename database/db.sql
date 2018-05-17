create table `video_rtmp_to_video` (
  `id` bigint(20) not null auto_increment comment '主健',
  `url` varchar(255) not null comment '视频下载链接',
  `rid` integer(12) not null comment '房间号',
  `fsize` bigint(20) not null comment '视频大小',
  `starttime` integer(12) not null comment '运营商',
  `endtime` integer(12) not null comment 'ip范围',
  primary key (`id`),
  key `ix_rid` (`rid`),
  key `ix_starttime` (`starttime`),
  key `ix_endtime` (`endtime`)
) engine=InnoDB default charset=utf8 comment='网宿视频录像';