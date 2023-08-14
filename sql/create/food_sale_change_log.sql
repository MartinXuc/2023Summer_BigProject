drop table if exists `food_sale_change_log`;
create table `food_sale_change_log`  (
  `id` int(0) unsigned not null auto_increment,
  `food_id` int(0) not null default 0 comment '商品id',
  `quantity` int(0) not null default 0 comment '售卖数量',
  `price` decimal(10, 2) not null comment '售卖金额',
  `member_id` int(0) not null default 0 comment '会员id',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '售卖时间',
  primary key (`id`) using btree,
  index `idx_food_id_id`(`food_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '商品销售情况' row_format = dynamic;
