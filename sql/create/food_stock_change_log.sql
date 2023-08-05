drop table if exists `food_stock_change_log`;
create table `food_stock_change_log`  (
  `id` int(0) unsigned not null auto_increment,
  `food_id` int(0) not null comment 'food_id',
  `unit` int(0) not null default 0 comment '改变量',
  `total_stock` int(0) not null default 0 comment '变更后总量',
  `note` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '备注字段',
  `created_time` datetime(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_food_id`(`food_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '数据库存变更表' row_format = dynamic;
