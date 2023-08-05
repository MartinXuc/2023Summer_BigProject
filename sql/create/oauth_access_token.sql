drop table if exists `oauth_access_token`;
create table `oauth_access_token`  (
  `id` int(0) unsigned not null auto_increment,
  `access_token` varchar(600) character set utf8mb4 collate utf8mb4_general_ci not null default '',
  `expired_time` timestamp(0) not null default current_timestamp(0) comment '过期时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_expired_time`(`expired_time`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '微信的access_token 用户调用其他接口的' row_format = dynamic;
