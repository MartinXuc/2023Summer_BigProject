drop table if exists `queue_list`;
create table `queue_list`  (
  `id` int(0) unsigned not null auto_increment,
  `queue_name` varchar(30) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '队列名字',
  `data` varchar(500) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '队列数据',
  `status` tinyint(1) not null default -1 comment '状态 -1 待处理 1 已处理',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '事件队列表' row_format = dynamic;
