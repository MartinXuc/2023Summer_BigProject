drop table if exists `wx_share_history`;
create table `wx_share_history`  (
  `id` int(0) unsigned not null auto_increment,
  `member_id` int(0) not null default 0 comment '会员id',
  `share_url` varchar(200) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '分享的页面url',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '创建时间',
  primary key (`id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '微信分享记录' row_format = dynamic;
