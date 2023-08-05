drop table if exists `app_error_log`;
create table `app_error_log`  (
  `id` int(0) unsigned not null auto_increment,
  `referer_url` varchar(255) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '当前访问的refer',
  `target_url` varchar(255) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '访问的url',
  `query_params` text character set utf8mb4 collate utf8mb4_general_ci not null comment 'get和post参数',
  `content` longtext character set utf8mb4 collate utf8mb4_general_ci not null comment '日志内容',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = 'app错误日表' row_format = dynamic;
