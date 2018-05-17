create table `video_rtmp_to_video` (
  `id` bigint(20) not null auto_increment comment '����',
  `url` varchar(255) not null comment '��Ƶ��������',
  `rid` integer(12) not null comment '�����',
  `fsize` bigint(20) not null comment '��Ƶ��С',
  `starttime` integer(12) not null comment '��Ӫ��',
  `endtime` integer(12) not null comment 'ip��Χ',
  primary key (`id`),
  key `ix_rid` (`rid`),
  key `ix_starttime` (`starttime`),
  key `ix_endtime` (`endtime`)
) engine=InnoDB default charset=utf8 comment='������Ƶ¼��';