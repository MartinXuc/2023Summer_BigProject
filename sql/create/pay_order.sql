drop table if exists `pay_order`;
create table `pay_order`  (
  `id` int(0) unsigned not null auto_increment,
  `order_sn` varchar(40) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '随机订单号',
  `member_id` bigint(0) not null default 0 comment '会员id',
  `total_price` decimal(10, 2) not null comment '订单应付金额',
  `yun_price` decimal(10, 2) not null comment '运费金额',
  `pay_price` decimal(10, 2) not null comment '订单实付金额',
  `pay_sn` varchar(128) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '第三方流水号',
  `prepay_id` varchar(128) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '第三方预付id',
  `note` text character set utf8mb4 collate utf8mb4_general_ci not null comment '备注信息',
  `status` tinyint(0) not null default 0 comment '1:支付完成 0 无效 -1 申请退款 -2 退款中 -9 退款成功  -8 待支付  -7 完成支付待确认',
  `express_status` tinyint(0) not null default 0 comment '快递状态，-8 待支付 -7 已付款待发货 1:确认收货 0:失败',
  `express_address_id` int(0) not null default 0 comment '快递地址id',
  `express_info` varchar(1000) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '快递信息',
  `comment_status` tinyint(1) not null default 0 comment '评论状态',
  `pay_time` timestamp(0) not null default current_timestamp(0) comment '付款到账时间',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最近一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  unique index `idx_order_sn`(`order_sn`) using btree,
  index `idx_member_id_status`(`member_id`, `status`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '在线购买订单表' row_format = dynamic;
