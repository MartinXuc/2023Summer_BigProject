drop table if exists `pay_order_callback_data`;
create table `pay_order_callback_data`  (
  `id` int(0) not null auto_increment,
  `pay_order_id` int(0) not null default 0 comment '支付订单id',
  `pay_data` text character set utf8mb4 collate utf8mb4_general_ci not null comment '支付回调信息',
  `refund_data` text character set utf8mb4 collate utf8mb4_general_ci not null comment '退款回调信息',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '创建时间',
  primary key (`id`) using btree,
  unique index `pay_order_id`(`pay_order_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci row_format = dynamic;
