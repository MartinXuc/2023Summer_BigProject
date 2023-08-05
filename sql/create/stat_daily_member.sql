drop table if exists `stat_daily_member`;
create table `stat_daily_member`  (
  `id` int(0) unsigned not null auto_increment,
  `date` date not null comment '日期',
  `member_id` int(0) not null default 0 comment '会员id',
  `total_shared_count` int(0) not null default 0 comment '当日分享总次数',
  `total_pay_money` decimal(10, 2) not null comment '当日付款总金额',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_date_member_id`(`date`, `member_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '会员日统计' row_format = dynamic;
