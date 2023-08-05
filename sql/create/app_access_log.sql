drop table if exists `app_access_log`;

create table `app_access_log`  (
  `id` int(0) not null auto_increment,
  `uid` bigint(0) not null default 0 comment 'uid',
  `referer_url` varchar(255) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '当前访问的refer',
  `target_url` varchar(255) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '访问的url',
  `query_params` text character set utf8mb4 collate utf8mb4_general_ci not null comment 'get和post参数',
  `ua` varchar(1024) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '访问ua',
  `ip` varchar(32) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '访问ip',
  `note` varchar(1000) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment 'json格式备注字段',
  `created_time` timestamp(0) not null default current_timestamp(0),
  primary key (`id`) using btree,
  index `idx_uid`(`uid`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '用户访问记录表' row_format = dynamic;
