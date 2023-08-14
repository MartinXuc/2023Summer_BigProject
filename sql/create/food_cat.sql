drop table if exists `food_cat`;
create table `food_cat`  (
  `id` int(0) unsigned not null auto_increment,
  `name` varchar(50) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '类别名称',
  `weight` tinyint(0) not null default 1 comment '权重',
  `status` tinyint(1) not null default 1 comment '状态 1:有效 0:无效',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  unique index `idx_name`(`id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '食品分类' row_format = dynamic;
