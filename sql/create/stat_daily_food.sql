drop table if exists `stat_daily_food`;
create table `stat_daily_food`  (
  `id` int(0) unsigned not null auto_increment,
  `date` date not null,
  `food_id` int(0) not null default 0 comment '菜品id',
  `total_count` int(0) not null default 0 comment '售卖总数量',
  `total_pay_money` decimal(10, 2) not null comment '总售卖金额',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `date_food_id`(`date`, `food_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '书籍售卖日统计' row_format = dynamic;
