drop table if exists `member_address`;
create table `member_address`  (
  `id` int(0) unsigned not null auto_increment,
  `member_id` int(0) not null default 0 comment '会员id',
  `name` varchar(20) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '收货人姓名',
  `mobile` varchar(11) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '收货人手机号码',
  `province_id` int(0) not null default 0 comment '省id',
  `province_str` varchar(50) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '省名称',
  `city_id` int(0) not null default 0 comment '城市id',
  `city_str` varchar(50) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '市名称',
  `area_id` int(0) not null default 0 comment '区域id',
  `area_str` varchar(50) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '区域名称',
  `address` varchar(100) character set utf8mb4 collate utf8mb4_general_ci not null default '' comment '详细地址',
  `status` tinyint(1) not null default 1 comment 'status 1:valid 0:invalid',
  `is_default` tinyint(1) not null default 0 comment '默认地址',
  `updated_time` timestamp(0) not null default current_timestamp(0) comment '最后一次更新时间',
  `created_time` timestamp(0) not null default current_timestamp(0) comment '插入时间',
  primary key (`id`) using btree,
  index `idx_member_id_status`(`member_id`, `status`) using btree
) engine = innodb character set = utf8mb4 collate = utf8mb4_general_ci comment = '会员收货地址' row_format = dynamic;
