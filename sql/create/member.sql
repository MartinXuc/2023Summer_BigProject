drop table if exists `member`;
create table `member`  (
  `id` int(0) unsigned not null auto_increment,
  `openid` varchar(80) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment 'wechat_id',
  `name` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '会员名',
  `mobile` varchar(11) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '会员手机号码',
  `sex` tinyint(1) not null default 0 comment '1 represents male, 2 represents female, else represents unknown',
  `avatar` varchar(200) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '会员头像',
  `salt` varchar(32) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '随机salt',
  `reg_ip` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '注册ip',
  `status` tinyint(1) not null default 1 comment 'status 1:valid 0:invalid',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '会员表' row_format = dynamic;
