drop table if exists `member_cart`;
create table `member_cart`  (
  `id` int(0) unsigned not null auto_increment,
  `member_id` bigint(0) not null default 0 comment '会员id',
  `food_id` int(0) not null default 0 comment '图书id',
  `quantity` int(0) not null default 0 comment '数量',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_member_id`(`member_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '购物车' row_format = dynamic;
