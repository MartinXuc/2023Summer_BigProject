drop table if exists `images`;
create table `images`  (
  `id` int(0) unsigned not null auto_increment,
  `file_key` varchar(60) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '文件名',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci row_format = dynamic;
