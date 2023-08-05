drop table if exists `pay_order_item`;
create table `pay_order_item`  (
  `id` int(0) unsigned not null auto_increment,
  `pay_order_id` int(0) not null default 0 comment '订单id',
  `member_id` bigint(0) not null default 0 comment '会员id',
  `quantity` int(0) not null default 1 comment '购买数量 默认1份',
  `price` decimal(10, 2) not null comment '商品总价格，售价 * 数量',
  `food_id` int(0) not null default 0 comment '美食表id',
  `note` text character set utf8mb4 collate utf8mb4_general_ci not null comment '备注信息',
  `status` tinyint(1) not null default 1 comment '状态:1:成功 0 失败',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最近一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_member_id`(`food_id`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '订单详情表' row_format = dynamic;
