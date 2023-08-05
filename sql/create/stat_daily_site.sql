drop table if exists `stat_daily_site`;
create table `stat_daily_site`  (
  `id` int(0) unsigned not null auto_increment,
  `date` date not null comment '日期',
  `total_pay_money` decimal(10, 2) not null comment '当日应收总金额',
  `total_member_count` int(0) not null comment '会员总数',
  `total_new_member_count` int(0) not null comment '当日新增会员数',
  `total_order_count` int(0) not null comment '当日订单数',
  `total_shared_count` int(0) not null,
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_date`(`date`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '全站日统计' row_format = dynamic;
